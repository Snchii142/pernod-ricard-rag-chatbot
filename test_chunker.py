from src.chunker import load_documents
from src.chunker import chunk_documents

documents = load_documents()

chunks = chunk_documents(documents)

print("Documents:", len(documents))
print("Chunks:", len(chunks))

print("\nExample Chunk:\n")

print(chunks[0])