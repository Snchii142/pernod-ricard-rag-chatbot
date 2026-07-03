from src.retriever import HybridRetriever

retriever = HybridRetriever()

results = retriever.hybrid_search(
    "Tell me about Jameson"
)

print()

print("Retrieved:", len(results))

print()

for r in results:

    print("=" * 60)

    print(r["metadata"]["brand"])

    print(r["metadata"]["title"])

    print()

    print(r["text"][:250])