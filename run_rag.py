"""
Main entry point for the Pernod Ricard RAG Chatbot.
"""
from src.utils import format_sources
from src.retriever import HybridRetriever
from src.llm import generate_answer


def main():

    retriever = HybridRetriever()

    print("=" * 70)
    print("Pernod Ricard RAG Chatbot")
    print("Type 'exit' to quit.")
    print("=" * 70)

    while True:

        query = input("\nYou: ")

        if query.lower() in ["exit", "quit"]:

            print("\nGoodbye!")

            break

        print("\nSearching knowledge base...")

        retrieved_chunks = retriever.hybrid_search(
            query=query,
            k=5
        )

        print("Generating answer...\n")

        try:

            answer = generate_answer(
                query,
                retrieved_chunks
            )

            print("=" * 70)
            print(answer)
            print("=" * 70)

            print(format_sources(retrieved_chunks))

        except Exception as e:

            print("\nLLM Error:")
            print(e)

            print("\nRetrieved Sources:\n")
            print(format_sources(retrieved_chunks))


if __name__ == "__main__":
    main()