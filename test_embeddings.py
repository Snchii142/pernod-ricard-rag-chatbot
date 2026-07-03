from src.embeddings import embed_text

embedding = embed_text("Pernod Ricard is a global spirits company.")

print("Embedding dimension:", len(embedding))
print("First 10 values:", embedding[:10])