from src.retriever import HybridRetriever
from src.llm import generate_answer

retriever = HybridRetriever()

query = "Tell me about Jameson."

results = retriever.hybrid_search(query)

answer = generate_answer(
    query,
    results
)

print("\n")
print("=" * 80)
print(answer)
print("=" * 80)