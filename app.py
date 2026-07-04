"""
Pernod Ricard Knowledge Assistant
Premium Enterprise UI
"""

import time
import streamlit as st

from run_rag import ask_question


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="Pernod Ricard Knowledge Assistant",
    page_icon="🥃",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CACHE
# ---------------------------------------------------------

@st.cache_resource
def load_chatbot():
    return ask_question

chatbot = load_chatbot()

# ---------------------------------------------------------
# WELCOME MESSAGE
# ---------------------------------------------------------

WELCOME_MESSAGE = """
👋 **Welcome to the Pernod Ricard Knowledge Assistant**

I'm an enterprise AI assistant powered by **Hybrid Retrieval-Augmented Generation (RAG).**

You can ask me about:

- 🥃 Pernod Ricard Brands
- 🌍 Sustainability
- 🏢 Company Information
- 🍸 Responsible Drinking

Every answer is generated using the knowledge base and includes supporting sources whenever available.
"""

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

/* ---------- Background ---------- */

.stApp{

background:
linear-gradient(
135deg,
#08121F 0%,
#111827 55%,
#1B263B 100%
);

color:white;

}


/* ---------- Main ---------- */

.block-container{

padding-top:2rem;
padding-left:2.5rem;
padding-right:2.5rem;
padding-bottom:2rem;

}


/* ---------- Sidebar ---------- */

[data-testid="stSidebar"]{

background:
linear-gradient(
180deg,
#0D1525,
#172235
);

border-right:1px solid rgba(255,255,255,.08);

}


/* ---------- Cards ---------- */

.glass-card{

background:rgba(255,255,255,.08);

backdrop-filter:blur(18px);

border-radius:20px;

padding:20px;

border:1px solid rgba(255,255,255,.08);

box-shadow:
0 8px 30px rgba(0,0,0,.35);

margin-bottom:15px;

}


/* ---------- Chat ---------- */

[data-testid="stChatMessage"]{

background:rgba(255,255,255,.05);

border-radius:18px;

padding:15px;

border:1px solid rgba(255,255,255,.08);

margin-bottom:18px;

transition:.25s;

}

[data-testid="stChatMessage"]:hover{

transform:translateY(-2px);

}


/* ---------- Header ---------- */

.title{

font-size:42px;

font-weight:800;

color:white;

margin-bottom:6px;

}

.subtitle{

font-size:17px;

color:#d6d6d6;

margin-bottom:30px;

}


/* ---------- Metrics ---------- */

.metric-card{

background:rgba(255,255,255,.07);

border-radius:18px;

padding:20px;

text-align:center;

border:1px solid rgba(255,255,255,.08);

transition:.3s;

}

.metric-card:hover{

transform:translateY(-5px);

}


/* ---------- Buttons ---------- */

.stButton>button{

width:100%;

background:
linear-gradient(
90deg,
#8B0000,
#C8102E
);

color:white;

font-weight:bold;

border:none;

border-radius:12px;

padding:.75rem;

transition:.3s;

}

.stButton>button:hover{

transform:scale(1.02);

box-shadow:0 0 18px rgba(200,16,46,.45);

}


/* ---------- Footer ---------- */

footer{

visibility:hidden;

}

#MainMenu{

visibility:hidden;

}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown("## 🥃 Pernod Ricard")

    st.caption("Enterprise Knowledge Assistant")

    st.markdown("---")

    # ---------------------------------------------------------
# RECENT CHAT HISTORY
# ---------------------------------------------------------

    st.subheader("💬 Recent Chat")

    history = [
        msg["content"]
        for msg in st.session_state.get("messages", [])
        if msg["role"] == "user"
    ]

    if history:

        for i, question in enumerate(reversed(history[-5:]), 1):

            st.caption(f"{i}. {question[:45]}...")

    else:

        st.caption("No conversations yet.")

        st.subheader("💡 Suggested Questions")

        suggestions = [
            "Tell me about Jameson",
            "What is Absolut Vodka?",
            "What brands does Pernod Ricard own?",
            "Tell me about Chivas Regal",
            "Describe Ballantine's whisky"
        ]

        for question in suggestions:
            st.button(
                question,
                key=f"suggestion_{question}",
                disabled=True,
                use_container_width=True
            )

    st.markdown("---")


    st.subheader("🛡 Responsible AI")

    age_confirmed = st.checkbox(
        "I confirm I am above the legal drinking age."
    )

    st.info(
        """
Please drink responsibly.

This assistant does **not** provide:

• Medical advice

• Purchasing advice

• Legal advice
"""
    )

    st.markdown("---")

    if st.button(
        "🗑 Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": WELCOME_MESSAGE
            }
        ]

        st.rerun()


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    """
<div class='title'>
🥃 Pernod Ricard Knowledge Assistant
</div>
""",
    unsafe_allow_html=True
)

st.markdown(
    """
<div class='subtitle'>
Enterprise Retrieval-Augmented Generation (RAG) Assistant powered by Hybrid Search,
ChromaDB and Large Language Models.
</div>
""",
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# DASHBOARD
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(
        """
<div class="metric-card">

### 📄 Documents

Knowledge Base

</div>
""",
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
<div class="metric-card">

### 🥃 Brands

240+

</div>
""",
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
<div class="metric-card">

### 🔍 Retrieval

Hybrid Search

</div>
""",
        unsafe_allow_html=True
    )

with col4:

    st.markdown(
        """
<div class="metric-card">

### 🤖 LLM

Groq Llama 3.3

</div>
""",
        unsafe_allow_html=True
    )

st.write("")


# ---------------------------------------------------------
# WELCOME CARD
# ---------------------------------------------------------


st.write("")


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = [

        {
            "role": "assistant",
            "content": WELCOME_MESSAGE
        }

    ]


# ---------------------------------------------------------
# CHAT HISTORY
# ---------------------------------------------------------

chat_container = st.container()

with chat_container:

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

            if message.get("sources"):

                with st.expander("📚 View Sources", expanded=False):

                    st.markdown(message["sources"])


# ---------------------------------------------------------
# USER INPUT
# ---------------------------------------------------------

# ---------------------------------------------------------
# CHAT INPUT
# ---------------------------------------------------------

if not age_confirmed:

    st.warning(
        "⚠️ Please confirm that you are above the legal drinking age to start chatting."
    )

    prompt = None

    st.chat_input(
        "Please confirm your age in the sidebar...",
        disabled=True
    )

else:

    prompt = st.chat_input(
        "Ask about Pernod Ricard brands, sustainability, company information..."
    )

# ---------------------------------------------------------
# PROCESS USER QUERY
# ---------------------------------------------------------

if prompt:

    if not age_confirmed:

        st.warning(
            "⚠️ Please confirm that you are above the legal drinking age before using the assistant."
        )

        st.stop()

    # Save user message

    st.session_state.messages.append(

        {
            "role": "user",
            "content": prompt
        }

    )

    with st.chat_message("user"):

        st.markdown(prompt)

    # Assistant

    with st.chat_message("assistant"):

        thinking = st.empty()

        thinking.markdown(
            """
🤖 **Searching knowledge base...**

Please wait...
"""
        )

        start = time.time()

        try:

            result = chatbot(prompt)

            elapsed = time.time() - start

            thinking.empty()

            st.markdown(result["answer"])

            col1, col2 = st.columns([3,1])

            with col1:

                st.caption(
                    f"⏱ Response generated in **{elapsed:.2f} sec**"
                )

            with col2:

                if result["success"]:

                    st.success("Retrieved")

                else:

                    st.warning("Guardrail")

            if result["sources"]:

                with st.expander(
                    "📚 Sources Used",
                    expanded=False
                ):

                    st.markdown(result["sources"])

            st.session_state.messages.append(

                {
                    "role": "assistant",
                    "content": result["answer"],
                    "sources": result["sources"]
                }

            )

        except Exception as e:

            thinking.empty()

            st.error(
                "Unable to generate a response."
            )

            st.exception(e)

            st.session_state.messages.append(

                {
                    "role":"assistant",

                    "content":
                    "Unable to generate a response."
                }

            )
