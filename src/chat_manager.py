"""
Chat History Manager using ChromaDB.

This module manages:
1. Chat sessions
2. Individual chat messages
"""

import uuid
from datetime import datetime

from src.vectordb import client

# ---------------------------------------------------------
# Collections
# ---------------------------------------------------------

chat_collection = client.get_or_create_collection(
    name="chat_history"
)

message_collection = client.get_or_create_collection(
    name="chat_messages"
)


# ---------------------------------------------------------
# Create New Chat
# ---------------------------------------------------------

def create_chat(title="New Chat"):

    chat_id = str(uuid.uuid4())

    chat_collection.add(

        ids=[chat_id],

        documents=[title],

        metadatas=[

            {

                "title": title,

                "created_at": datetime.now().isoformat(),

                "updated_at": datetime.now().isoformat()

            }

        ]

    )

    return chat_id


# ---------------------------------------------------------
# Save Message
# ---------------------------------------------------------

def save_message(chat_id, role, message):

    message_id = str(uuid.uuid4())

    message_collection.add(

        ids=[message_id],

        documents=[message],

        metadatas=[

            {

                "chat_id": chat_id,

                "role": role,

                "timestamp": datetime.now().isoformat()

            }

        ]

    )

    # Update chat timestamp

    chat = chat_collection.get(ids=[chat_id])

    if chat["ids"]:

        metadata = chat["metadatas"][0]

        metadata["updated_at"] = datetime.now().isoformat()

        chat_collection.update(

            ids=[chat_id],

            documents=chat["documents"],

            metadatas=[metadata]

        )


# ---------------------------------------------------------
# Load Messages
# ---------------------------------------------------------

def load_chat(chat_id):

    results = message_collection.get(

        where={

            "chat_id": chat_id

        },

        include=[

            "documents",

            "metadatas"

        ]

    )

    messages = []

    docs = results["documents"]
    metas = results["metadatas"]

    combined = list(zip(docs, metas))

    combined.sort(

        key=lambda x: x[1]["timestamp"]

    )

    for doc, meta in combined:

        messages.append(

            {

                "role": meta["role"],

                "content": doc

            }

        )

    return messages


# ---------------------------------------------------------
# List Chats
# ---------------------------------------------------------

def get_all_chats():

    chats = chat_collection.get(

        include=[

            "documents",

            "metadatas"

        ]

    )

    chat_list = []

    docs = chats["documents"]
    metas = chats["metadatas"]
    ids = chats["ids"]

    for chat_id, title, meta in zip(ids, docs, metas):

        chat_list.append(

            {

                "chat_id": chat_id,

                "title": title,

                "updated_at": meta["updated_at"]

            }

        )

    chat_list.sort(

        key=lambda x: x["updated_at"],

        reverse=True

    )

    return chat_list


# ---------------------------------------------------------
# Rename Chat
# ---------------------------------------------------------

def rename_chat(chat_id, new_title):

    chat = chat_collection.get(ids=[chat_id])

    if not chat["ids"]:

        return

    metadata = chat["metadatas"][0]

    metadata["updated_at"] = datetime.now().isoformat()

    chat_collection.update(

        ids=[chat_id],

        documents=[new_title],

        metadatas=[metadata]

    )


# ---------------------------------------------------------
# Delete Chat
# ---------------------------------------------------------

def delete_chat(chat_id):

    chat_collection.delete(

        ids=[chat_id]

    )

    messages = message_collection.get(

        where={

            "chat_id": chat_id

        }

    )

    if messages["ids"]:

        message_collection.delete(

            ids=messages["ids"]

        )