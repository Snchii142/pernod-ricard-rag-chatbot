"""
Gemini LLM interface for the Pernod Ricard RAG Chatbot.

Uses the new google-genai SDK.

NOTE:
The assignment requires Gemini 1.5 Pro.
The model can be switched back to Gemini 1.5 Pro
once API quota/access is available.
"""

import os

from google import genai
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
# Initialise Client
# ---------------------------------------------------

client = genai.Client(
    api_key=API_KEY,
    http_options={"api_version": "v1"}
)

# Change this back to gemini-1.5-pro once your project
# has access to that model.
MODEL = "gemini-2.0-flash"


# ---------------------------------------------------
# Generate Answer
# ---------------------------------------------------

def generate_answer(question: str, retrieved_chunks: list) -> str:
    """
    Generate answer using retrieved context.
    """

    if not retrieved_chunks:
        return (
            "I'm sorry, I couldn't find relevant information in the current knowledge base."
        )

    context = "\n\n".join(
        chunk["text"] for chunk in retrieved_chunks
    )

    prompt = f"""
{SYSTEM_PROMPT}

-------------------------
RETRIEVED CONTEXT
-------------------------

{context}

-------------------------
USER QUESTION
-------------------------

{question}

Answer:
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=1024,
        ),
    )

    return response.text