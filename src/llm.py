"""
Gemini LLM interface.

Uses the new google-genai SDK.

NOTE:
The assignment requires Gemini 1.5 Pro.
The model identifier may be switched back to Gemini 1.5 Pro
once API quota/access is available.
"""

import os

from google import genai                   # NEW package (pip install google-genai)
from google.genai import types

from dotenv import load_dotenv

from src.prompts import SYSTEM_PROMPT


# ---------------------------------------------------
# Load API Key
# ---------------------------------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")


# ---------------------------------------------------
# Initialise Client  ← new SDK uses Client, not configure()
# ---------------------------------------------------

client = genai.Client(
    api_key=API_KEY,
    http_options={"api_version": "v1"}
)
MODEL = "gemini-2.0-flash"          # same model, new SDK finds it correctly


# ---------------------------------------------------
# Generate Answer
# ---------------------------------------------------

def generate_answer(question: str, retrieved_chunks: list) -> str:
    """
    Generate answer using retrieved context.

    Args:
        question:          User's query string
        retrieved_chunks:  List of dicts with key "text" from retriever

    Returns:
        LLM response as plain string
    """

    # Handle empty retrieval gracefully (hallucination guardrail)
    if not retrieved_chunks:
        return (
            "I'm sorry, I don't have specific information about that in my "
            "current knowledge base. For accurate details, please visit "
            "pernod-ricard.com or the relevant brand website directly."
        )

    context = "\n\n".join(
        chunk["text"] for chunk in retrieved_chunks
    )

    prompt = f"""\
{SYSTEM_PROMPT}

-------------------------
RETRIEVED CONTEXT
-------------------------

{context}

-------------------------
USER QUESTION
-------------------------

{question}

Answer:"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,      # lower = more factual, less hallucination
            max_output_tokens=1024,
        ),
    )

    return response.text