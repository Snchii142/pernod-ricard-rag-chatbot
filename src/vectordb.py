"""
Vector database using ChromaDB.
"""

import chromadb

from chromadb.config import Settings


# -----------------------------------------
# Create / Load Persistent ChromaDB
# -----------------------------------------

client = chromadb.PersistentClient(path="vectorstore")

collection = client.get_or_create_collection(
    name="pernod_ricard_knowledge"
)


# -----------------------------------------
# Add chunks into ChromaDB
# -----------------------------------------

def add_chunks(embedded_chunks):

    # Check whether collection already has data
    if collection.count() > 0:
        print("⚠️ ChromaDB already contains data.")
        print("Skipping insertion.")
        return

    ids = []
    documents = []
    embeddings = []
    metadatas = []

    for chunk in embedded_chunks:

        ids.append(f"chunk_{chunk['chunk_id']}")

        documents.append(chunk["text"])

        embeddings.append(chunk["embedding"])

        metadatas.append({

            "brand": chunk["brand"],

            "category": chunk["category"],

            "title": chunk["title"],

            "url": chunk["url"]

        })

    collection.add(

        ids=ids,

        documents=documents,

        embeddings=embeddings,

        metadatas=metadatas

    )

    print(f"\n✅ Stored {len(ids)} chunks in ChromaDB")


# -----------------------------------------
# Retrieve collection
# -----------------------------------------

def get_collection():

    return collection