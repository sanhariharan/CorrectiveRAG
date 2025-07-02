# CorrectiveRAG

CorrectiveRAG is a Retrieval-Augmented Generation (RAG) project that leverages LangChain, LangGraph, and advanced AI models to perform intelligent document retrieval and generation. The system loads data from web sources, processes it with language models, and uses embeddings and vector stores to enhance retrieval capabilities.

## Architecture

The architecture of CorrectiveRAG is illustrated in the following diagram:

![Architecture Workflow](../Workflow.png)

This workflow demonstrates the data loading, processing, embedding, and retrieval steps that form the core of the RAG system.

## Technology Stack

The project uses the following technology stack:

- **LangChain & LangGraph** for building language model applications and graph-based workflows.
- **Google Generative AI Embeddings** for creating semantic embeddings.
- **Groq LLM** for chat-based language modeling.
- **ChromaDB** as the vector store for efficient similarity search.
- **Tavily** for web search tool integration.
- **Python-dotenv** for environment variable management.
- **FastAPI, Uvicorn, Streamlit** (optional) for serving and UI.

### Stack Images

Below are images representing the main technologies used in the project:

![LangChain Logo](./images/langchain.png)  
![Groq Logo](./images/groq.png)  
![ChromaDB Logo](./images/chromadb.png)  
![Google Generative AI Logo](./images/google-genai.png)  

*(Note: Replace the above image paths with actual images in the `images` folder.)*

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

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
