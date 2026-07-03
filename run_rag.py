"""
Main entry point for the Pernod Ricard RAG Chatbot.
"""

from src.guardrails import GuardrailEngine
from src.utils import format_sources
from src.retriever import HybridRetriever
from src.llm import generate_answer

# Initialize once so they are reused
retriever = HybridRetriever()
guard = GuardrailEngine()


def ask_question(query):
    """
    Processes a user query and returns the chatbot response.

    Returns:
        dict:
        {
            "success": bool,
            "answer": str,
            "sources": str
        }
    """

    allowed, message = guard.validate(query)

    if not allowed:
        return {
            "success": False,
            "answer": message,
            "sources": ""
        }

    retrieved_chunks = retriever.hybrid_search(
        query=query,
        k=5
    )

    answer = generate_answer(
        query=query,
        retrieved_chunks=retrieved_chunks
    )

    return {
        "success": True,
        "answer": answer,
        "sources": format_sources(retrieved_chunks)
    }


def main():

    print("=" * 70)
    print("Pernod Ricard RAG Chatbot")
    print("Type 'exit' to quit.")
    print("=" * 70)

    while True:

        query = input("\nYou: ").strip()

        if query.lower() in ["exit", "quit"]:

            print("\nGoodbye!")

            break

        try:

            print("\nSearching knowledge base...\n")

            result = ask_question(query)

            print("=" * 70)
            print(result["answer"])
            print("=" * 70)

            if result["sources"]:
                print(result["sources"])

        except Exception as e:

            print("\nLLM Error:")
            print(e)


if __name__ == "__main__":
    main()