"""
Chunk documents for RAG.

Uses section-aware splitting first,
then RecursiveCharacterTextSplitter
for oversized sections.
"""

import os
import json

from langchain_text_splitters import RecursiveCharacterTextSplitter


# ----------------------------
# Chunking configuration
# ----------------------------

CHUNK_SIZE = 800
CHUNK_OVERLAP = 150


splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators=[
        "\n\n",
        "\n",
        ". ",
        "? ",
        "! ",
        " ",
        ""
    ]
)


# ----------------------------
# Load JSON documents
# ----------------------------

def load_documents(data_folder="data/raw"):
    """
    Load every JSON document from data/raw.
    """

    documents = []

    for root, _, files in os.walk(data_folder):

        for file in files:

            if file.endswith(".json"):

                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8") as f:

                    documents.append(json.load(f))

    return documents


# ----------------------------
# Section-aware splitting
# ----------------------------

def split_into_sections(text):
    """
    Split using blank lines first.

    Acts as lightweight semantic chunking.
    """

    sections = []

    for section in text.split("\n\n"):

        section = section.strip()

        if section:

            sections.append(section)

    return sections


# ----------------------------
# Chunk documents
# ----------------------------

def chunk_documents(documents):

    chunks = []

    chunk_id = 0

    for document in documents:

        sections = split_into_sections(document["text"])

        for section in sections:

            split_chunks = splitter.split_text(section)

            for chunk in split_chunks:

                chunk_id += 1

                chunks.append({

                    "chunk_id": chunk_id,

                    "text": chunk,

                    "brand": document["brand"],

                    "category": document["category"],

                    "title": document["title"],

                    "url": document["url"]

                })

    return chunks