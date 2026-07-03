from src.chunker import load_documents
from src.chunker import chunk_documents

from src.embeddings import embed_chunks

from src.vectordb import add_chunks

documents = load_documents()

chunks = chunk_documents(documents)

embedded_chunks = embed_chunks(chunks)

add_chunks(embedded_chunks)