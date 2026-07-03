"""
Embedding generation using BAAI/bge-small-en-v1.5
"""

from sentence_transformers import SentenceTransformer


# --------------------------------------------------
# Load embedding model once
# --------------------------------------------------

MODEL_NAME = "BAAI/bge-small-en-v1.5"

embedding_model = SentenceTransformer(MODEL_NAME)


# --------------------------------------------------
# Generate embedding for one chunk
# --------------------------------------------------

def embed_text(text):
    """
    Generate embedding for a single text.
    """

    embedding = embedding_model.encode(
        text,
        normalize_embeddings=True
    )

    return embedding.tolist()


# --------------------------------------------------
# Generate embeddings for all chunks
# --------------------------------------------------

def embed_chunks(chunks):
    """
    Add embeddings to every chunk.
    """

    embedded_chunks = []

    for chunk in chunks:

        embedded_chunks.append({

            "chunk_id": chunk["chunk_id"],

            "text": chunk["text"],

            "embedding": embed_text(chunk["text"]),

            "brand": chunk["brand"],

            "category": chunk["category"],

            "title": chunk["title"],

            "url": chunk["url"]

        })

    return embedded_chunks