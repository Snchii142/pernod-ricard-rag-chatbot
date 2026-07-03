"""
Hybrid Retriever

Combines:
1. Dense Retrieval (ChromaDB)
2. BM25 Retrieval
3. MMR Re-ranking
"""

import numpy as np

from rank_bm25 import BM25Okapi

from src.embeddings import embed_text, embedding_model
from src.vectordb import get_collection


class HybridRetriever:

    def __init__(self):
        """
        Initialize retriever.
        Loads Chroma collection and builds BM25 index.
        """

        self.collection = get_collection()

        data = self.collection.get(
            include=["documents", "metadatas"]
        )

        self.documents = data["documents"]
        self.metadata = data["metadatas"]

        tokenized_documents = [
            doc.lower().split()
            for doc in self.documents
        ]

        self.bm25 = BM25Okapi(tokenized_documents)

    # --------------------------------------------------

    def dense_search(
        self,
        query,
        k=5
    ):
        """
        Dense retrieval using ChromaDB.
        """

        query_embedding = embed_text(query)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )

        dense_results = []

        for i in range(len(results["documents"][0])):

            dense_results.append({

                "text": results["documents"][0][i],

                "metadata": results["metadatas"][0][i],

                "source": "dense"

            })

        return dense_results

    # --------------------------------------------------

    def bm25_search(
        self,
        query,
        k=5
    ):
        """
        Lexical retrieval using BM25.
        """

        tokens = query.lower().split()

        scores = self.bm25.get_scores(tokens)

        ranked = sorted(

            zip(
                scores,
                self.documents,
                self.metadata
            ),

            key=lambda x: x[0],

            reverse=True

        )

        bm25_results = []

        for score, doc, meta in ranked[:k]:

            bm25_results.append({

                "text": doc,

                "metadata": meta,

                "source": "bm25"

            })

        return bm25_results

    # --------------------------------------------------

    def mmr_rerank(
        self,
        query,
        candidates,
        top_k=5,
        lambda_param=0.7
    ):
        """
        Maximum Marginal Relevance Re-ranking.

        Balances:
        - Relevance
        - Diversity
        """

        if len(candidates) <= top_k:
            return candidates

        query_embedding = np.array(
            embed_text(query)
        )

        candidate_embeddings = [

            np.array(

                embedding_model.encode(

                    candidate["text"],

                    normalize_embeddings=True

                )

            )

            for candidate in candidates

        ]

        selected = []
        selected_embeddings = []

        similarities = [

            np.dot(query_embedding, embedding)

            for embedding in candidate_embeddings

        ]

        first_index = int(np.argmax(similarities))

        selected.append(
            candidates[first_index]
        )

        selected_embeddings.append(
            candidate_embeddings[first_index]
        )

        remaining = list(range(len(candidates)))

        remaining.remove(first_index)

        while len(selected) < min(top_k, len(candidates)):

            best_score = -1e9

            best_index = None

            for idx in remaining:

                relevance = np.dot(

                    query_embedding,

                    candidate_embeddings[idx]

                )

                diversity = max(

                    np.dot(

                        candidate_embeddings[idx],

                        selected_embedding

                    )

                    for selected_embedding in selected_embeddings

                )

                score = (

                    lambda_param * relevance

                    -

                    (1 - lambda_param) * diversity

                )

                if score > best_score:

                    best_score = score

                    best_index = idx

            selected.append(
                candidates[best_index]
            )

            selected_embeddings.append(
                candidate_embeddings[best_index]
            )

            remaining.remove(best_index)

        return selected

    # --------------------------------------------------

    def hybrid_search(
        self,
        query,
        k=5
    ):
        """
        Hybrid Retrieval:
        Dense + BM25 + MMR
        """

        dense_results = self.dense_search(
            query,
            k
        )

        bm25_results = self.bm25_search(
            query,
            k
        )

        merged = []

        seen = set()

        for result in dense_results + bm25_results:

            if result["text"] not in seen:

                merged.append(result)

                seen.add(result["text"])

        reranked = self.mmr_rerank(

            query,

            merged,

            top_k=k

        )

        return reranked