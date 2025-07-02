# 🤖 CorrectiveRAG — AI That Retrieves, Thinks, and Corrects

**CorrectiveRAG** is an advanced Retrieval-Augmented Generation (RAG) system designed to intelligently retrieve and generate answers from web and document-based sources using state-of-the-art LLMs, embeddings, and graph-based agents.

It leverages tools like **LangChain**, **LangGraph**, **Groq LLM**, **Google GenAI embeddings**, and **ChromaDB** to create a robust, modular, and production-ready RAG pipeline.

---

## 🧭 Architecture Overview

Below is the workflow representing how CorrectiveRAG operates internally:

![Architecture Workflow](./workflow.png)

This flow includes:

- 📰 Data ingestion from files or web
- 🧩 Chunking and embedding using **Google GenAI**
- 🧠 Multi-agent routing using **LangGraph**
- 🗃️ Vector similarity search with **ChromaDB**
- 🤖 Fast inference via **Groq LLM**
- 🌐 Optional web context from **Tavily Search**

---

## ⚙️ Technology Stack

CorrectiveRAG combines the best of open-source AI tooling and cloud-scale inference:

| Technology              | Purpose                                       | Logo |
|-------------------------|-----------------------------------------------|------|
| **LangChain**           | LLM framework & memory management             | ![LangChain Logo](./images/langchain.png) |
| **LangGraph**           | Graph-based multi-agent orchestration         | ![LangGraph Logo](./images/langgraph.png) |
| **Groq LLM**            | High-speed inference with low latency         | ![Groq Logo](./images/groq.png) |
| **Google GenAI**        | Semantic text embeddings for similarity search| ![Google Generative AI Logo](./images/google-genai.png) |
| **ChromaDB**            | Vector store for document chunks              | ![ChromaDB Logo](./images/chromadb.png) |
| **Tavily**              | Real-time web search integration              | ![Tavily Logo](./images/tavily.png) |

> ✅ Ensure the `images/` directory includes these logos for proper rendering in GitHub.

---

## 🚀 Installation Guide

Follow the steps below to set up CorrectiveRAG locally:

### 1. 📦 Clone the Repository

```bash
git clone <repository-url>
cd CorrectiveRAG
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Set up your environment variables in a `.env` file (create this file in the project root):

```
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

5. Run the main application:

```bash
python main.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

© 2024 CorrectiveRAG Project
