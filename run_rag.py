"""
Main entry point for the Pernod Ricard RAG Chatbot.
"""

from src.guardrails import GuardrailEngine
from src.utils import format_sources
from src.retriever import HybridRetriever
from src.llm import generate_answer

from src.chat_manager import (
    create_chat,
    save_message
)

# ---------------------------------------------------------
# Initialize
# ---------------------------------------------------------

retriever = HybridRetriever()
guard = GuardrailEngine()


# ---------------------------------------------------------
# Ask Question
# ---------------------------------------------------------

def ask_question(query, chat_id=None):

    """
    Processes a user query.

    Returns:
    {
        "success": bool,
        "answer": str,
        "sources": str,
        "chat_id": str
    }
    """

    # ----------------------------
    # Create chat if required
    # ----------------------------

    if chat_id is None:

        chat_id = create_chat(
            title=query[:40]
        )

    # ----------------------------
    # Save user message
    # ----------------------------

    save_message(

        chat_id,

        role="user",

        message=query

    )

    # ----------------------------
    # Guardrails
    # ----------------------------

    allowed, message = guard.validate(query)

    if not allowed:

        save_message(

            chat_id,

            role="assistant",

            message=message

        )

        return {

            "success": False,

            "answer": message,

            "sources": "",

            "chat_id": chat_id

        }

    # ----------------------------
    # Retrieval
    # ----------------------------

    retrieved_chunks = retriever.hybrid_search(

        query=query,

        k=5

    )
    # ---------------------------------------------------
     # Hallucination Boundary
    # ---------------------------------------------------

    if not retrieved_chunks:

        return {
            "success": False,

            "answer": (
                 "I couldn't find reliable information "
                "about that in the Pernod Ricard knowledge base."
            ),

            "sources": "",
            "chat_id": chat_id
        }

    # ----------------------------
    # LLM
    # ----------------------------

    answer = generate_answer(

        query,

        retrieved_chunks

    )

    # ----------------------------
    # Save assistant response
    # ----------------------------

    save_message(

        chat_id,

        role="assistant",

        message=answer

    )

    return {

        "success": True,

        "answer": answer,

        "sources": format_sources(

            retrieved_chunks

        ),

        "chat_id": chat_id

    }


# ---------------------------------------------------------
# CLI
# ---------------------------------------------------------

def main():

    chat_id = None

    print("=" * 70)
    print("Pernod Ricard Knowledge Assistant")
    print("Type 'exit' to quit.")
    print("=" * 70)

    while True:

        query = input("\nYou: ").strip()

        if query.lower() in ["exit", "quit"]:

            print("\nGoodbye!")

            break

        result = ask_question(

            query,

            chat_id

        )

        chat_id = result["chat_id"]

        print("=" * 70)
        print(result["answer"])
        print("=" * 70)

        if result["sources"]:

            print(result["sources"])


if __name__ == "__main__":
    main()