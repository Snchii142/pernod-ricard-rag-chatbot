# 🥃 Pernod Ricard Knowledge Assistant

An end-to-end **Retrieval-Augmented Generation (RAG)** chatbot built for **Pernod Ricard**. The assistant answers user queries using a curated company knowledge base while ensuring safe, grounded, and responsible responses through hybrid retrieval and rule-based guardrails.

---

## 📌 Overview

The chatbot combines document retrieval with a Large Language Model (LLM) to generate context-aware answers instead of relying solely on the model's internal knowledge.

The system first retrieves the most relevant information from the company's knowledge base using **Hybrid Search (Dense Retrieval + BM25)** and then generates an answer based only on the retrieved context. This significantly reduces hallucinations while providing transparent, source-backed responses.

---

## ✨ Features

- 📄 Automated web scraping of Pernod Ricard knowledge sources
- 🧹 Document cleaning and preprocessing
- ✂️ Intelligent document chunking
- 🧠 Sentence Transformer embeddings
- 🗂 ChromaDB Vector Database
- 🔍 Hybrid Retrieval (Dense Search + BM25)
- 🎯 MMR (Maximum Marginal Relevance) re-ranking
- 🤖 LLM-powered answer generation
- 🛡 Rule-based Guardrails
- 📚 Source attribution for every response
- 💬 Interactive Streamlit chat interface

---

## 🏗 Project Architecture

```
                    User Query
                         │
                         ▼
                Rule-based Guardrails
                         │
                         ▼
                Hybrid Retriever
        (Dense Retrieval + BM25 Search)
                         │
                         ▼
                   ChromaDB
                         │
                         ▼
              Retrieved Context
                         │
                         ▼
                Large Language Model
                         │
                         ▼
             Final Answer + Sources
```

---

## 🛡 Guardrails

The chatbot blocks or safely redirects queries involving:

- Unsafe alcohol consumption
- Medical advice
- Purchasing or pricing requests
- Competitor brand comparisons
- Out-of-scope queries
- Underage alcohol-related requests

---

## 🧰 Tech Stack

### Programming Language

- Python

### Backend

- ChromaDB
- Sentence Transformers
- rank-bm25
- BeautifulSoup
- Requests
- Streamlit

### Large Language Model

- Groq API (Llama 3.3-70B Versatile)

### Other Libraries

- python-dotenv
- tqdm
- NumPy

---

## 📂 Project Structure

```
pernod-ricard-rag-chatbot/

│
├── app.py                  # Streamlit application
├── run_rag.py              # Main RAG pipeline
├── requirements.txt
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scraper/
│
├── src/
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vectordb.py
│   ├── retriever.py
│   ├── prompts.py
│   ├── llm.py
│   ├── guardrails.py
│   └── utils.py
│
├── vectorstore/
│
└── tests/
```

---

## ⚙ Installation

Clone the repository

```bash
git clone <repository_url>
```

Navigate into the project

```bash
cd pernod-ricard-rag-chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_api_key
```

---

## ▶ Running the Application

Run the Streamlit interface

```bash
streamlit run app.py
```

Or run the CLI version

```bash
python run_rag.py
```

---

## 💬 Example Questions

- Tell me about Jameson.
- What brands does Pernod Ricard own?
- Describe Chivas Regal.
- What sustainability initiatives does Pernod Ricard have?
- Tell me about Absolut Vodka.
- Explain the history of Ballantine's.

---

## 🔄 RAG Pipeline

1. User submits a question.
2. Guardrails validate the request.
3. Hybrid Retrieval searches the knowledge base.
4. Relevant chunks are retrieved from ChromaDB.
5. MMR re-ranks the retrieved documents.
6. The LLM generates an answer using only the retrieved context.
7. Sources are displayed alongside the answer.

---

## 📸 User Interface

The application provides:

- Interactive chat interface
- Suggested questions
- Source citations
- Response latency
- Chat history
- Responsible drinking notice
- Age confirmation

---

## 🚀 Future Improvements

- Retrieval-aware guardrails
- Multi-LLM support (Gemini/OpenAI/Groq)
- Improved MMR optimization
- Better document deduplication
- Metadata-aware ranking
- Citation highlighting
- Docker deployment
- Unit and integration testing

---

## 👩‍💻 Author

Developed as part of an AI Engineering project for **Pernod Ricard**, demonstrating Retrieval-Augmented Generation (RAG), Hybrid Search, Guardrails, and Large Language Model integration.

---

## 📜 License

This project is intended for educational and demonstration purposes.