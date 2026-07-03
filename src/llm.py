"""
Groq LLM interface for the Pernod Ricard RAG Chatbot.
"""

import os

from dotenv import load_dotenv
from groq import Groq

from src.prompts import SYSTEM_PROMPT


# ---------------------------------------------------
# Load API Key
# ---------------------------------------------------

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env")


# ---------------------------------------------------
# Initialize Client
# ---------------------------------------------------

client = Groq(api_key=API_KEY)

MODEL = "llama-3.3-70b-versatile"


# ---------------------------------------------------
# Generate Answer
# ---------------------------------------------------

def generate_answer(question, retrieved_chunks):
    """
    Generate answer using retrieved context.
    """

    if not retrieved_chunks:
        return (
            "I couldn't find relevant information in the knowledge base."
        )

    context = "\n\n".join(
        chunk["text"]
        for chunk in retrieved_chunks
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
"""

    response = client.chat.completions.create(

        model=MODEL,

        temperature=0.2,

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],

        max_tokens=1024,

    )

    return response.choices[0].message.content