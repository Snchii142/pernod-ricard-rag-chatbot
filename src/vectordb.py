"""
Vector database using ChromaDB.
"""

import chromadb

# -----------------------------------------
# Create Persistent Client
# -----------------------------------------

client = chromadb.PersistentClient(
    path="vectorstore"
)

# -----------------------------------------
# Knowledge Collection
# -----------------------------------------

knowledge_collection = client.get_or_create_collection(
    name="pernod_ricard_knowledge"
)

# -----------------------------------------
# Chat History Collection
# -----------------------------------------

chat_collection = client.get_or_create_collection(
    name="chat_history"
)

# -----------------------------------------
# Add chunks into ChromaDB
# -----------------------------------------

def add_chunks(embedded_chunks):

    if knowledge_collection.count() > 0:

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

    knowledge_collection.add(

        ids=ids,

        documents=documents,

        embeddings=embeddings,

        metadatas=metadatas

    )

    print(f"Stored {len(ids)} chunks.")


# -----------------------------------------
# Getter
# -----------------------------------------

def get_collection():

    return knowledge_collection


def get_chat_collection():

    return chat_collection