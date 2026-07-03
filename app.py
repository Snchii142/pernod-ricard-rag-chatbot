"""
Streamlit UI for the Pernod Ricard Knowledge Assistant.
"""

import time
import streamlit as st

from run_rag import ask_question

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="Pernod Ricard Knowledge Assistant",
    page_icon="🥃",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# Custom CSS
# ----------------------------------------------------

st.markdown(
    """
<style>

.main {
    padding-top: 1rem;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.chat-title{
    font-size:36px;
    font-weight:bold;
    color:#8B0000;
}

.subtitle{
    color:gray;
    margin-bottom:25px;
}

footer{
    visibility:hidden;
}

#MainMenu{
    visibility:hidden;
}

</style>
""",
    unsafe_allow_html=True
)

# ----------------------------------------------------
# Cache Chatbot
# ----------------------------------------------------

@st.cache_resource
def load_chatbot():
    return ask_question


chatbot = load_chatbot()

WELCOME_MESSAGE = (
    "👋 **Welcome!**\n\n"
    "I'm the **Pernod Ricard Knowledge Assistant**.\n\n"
    "You can ask me about:\n"
    "- 🥃 Pernod Ricard brands\n"
    "- 🌍 Sustainability\n"
    "- 🏢 Company information\n"
    "- 🍸 Responsible drinking"
)

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/4/4b/Pernod_Ricard_logo.svg",
        width=180,
    )

    st.title("Knowledge Assistant")

    st.markdown("---")

    st.subheader("Suggested Questions")

    suggestions = [
        "Tell me about Jameson.",
        "What is Absolut Vodka?",
        "What brands does Pernod Ricard own?",
        "Tell me about Chivas Regal.",
        "Describe Ballantine's whisky."
    ]

    for question in suggestions:
        st.markdown(f"• {question}")

    st.markdown("---")

    st.subheader("About")

    st.write(
        """
This chatbot uses:

- ✅ Hybrid Retrieval
- ✅ ChromaDB Vector Store
- ✅ BM25 Search
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ Rule-based Guardrails
- ✅ Large Language Model
"""
    )

    st.markdown("---")

    age_confirmed = st.checkbox(
        "I confirm I am above the legal drinking age."
    )

    st.info(
        "Please drink responsibly.\n\n"
        "This chatbot does not provide medical, legal or purchasing advice."
    )

    st.markdown("---")

    if st.button("🗑 Clear Chat", use_container_width=True):

        st.session_state.messages = [

            {
                "role": "assistant",
                "content": WELCOME_MESSAGE
            }

        ]

        st.rerun()

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.markdown(
    '<div class="chat-title">🥃 Pernod Ricard Knowledge Assistant</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    'Ask questions about Pernod Ricard brands, products, sustainability and company knowledge.'
    '</div>',
    unsafe_allow_html=True,
)

# ----------------------------------------------------
# Session State
# ----------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = [

        {
            "role": "assistant",
            "content": WELCOME_MESSAGE
        }

    ]

# ----------------------------------------------------
# Display Chat History
# ----------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message.get("sources"):

            with st.expander("📚 Sources"):

                st.markdown(message["sources"])

# ----------------------------------------------------
# User Input
# ----------------------------------------------------

prompt = st.chat_input(
    "Ask your question..."
)

if prompt:

    if not age_confirmed:

        st.warning(
            "Please confirm that you are above the legal drinking age before chatting."
        )

        st.stop()

    # -------------------------
    # Show user message
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    # -------------------------
    # Assistant Response
    # -------------------------

    with st.chat_message("assistant"):

        start = time.time()

        with st.spinner("Searching knowledge base..."):

            try:

                result = chatbot(prompt)

                elapsed = time.time() - start

                st.markdown(result["answer"])

                st.caption(
                    f"⏱ Response generated in {elapsed:.2f} seconds"
                )

                if result["sources"]:

                    with st.expander("📚 Sources Used"):

                        st.markdown(result["sources"])

                st.session_state.messages.append(

                    {
                        "role": "assistant",
                        "content": result["answer"],
                        "sources": result["sources"]
                    }

                )

            except Exception:

                error_message = (
                    "⚠️ Unable to generate a response from the language model.\n\n"
                    "Please verify that your API key has sufficient quota or try again later."
                )

                st.error(error_message)

                st.session_state.messages.append(

                    {
                        "role": "assistant",
                        "content": error_message
                    }

                )

# ----------------------------------------------------
# Footer
# ----------------------------------------------------

st.markdown("---")

st.caption(
    "Powered by Hybrid RAG • ChromaDB • BM25 • Gemini"
)