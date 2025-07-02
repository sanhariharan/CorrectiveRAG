from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.tools.retriever import create_retriever_tool
from langgraph.prebuilt import ToolNode
from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph.message import add_messages
from langgraph.graph import END, START, StateGraph
from langgraph.prebuilt import tools_condition
from langchain_core.messages import AIMessage, HumanMessage
from langchain import hub
import warnings



import os
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
os.environ["TAVILY_API_KEY"]=os.getenv("TAVILY_API_KEY")

load_dotenv()
# A we are doing the rag we should first follow the rag architecture
# first we need to load the data
# we use a langchains document loader
url=https://bhavikjikadara.medium.com/exploring-the-different-types-of-rag-in-ai-c118edf6d73c
loader=WebBaseLoader(url)
# now loading the actual data
data=loader.load()  

#splitting and chunking the data
text_splitter=RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=1000,chunk_overlap=150)


#now lets create the llm model 
llm=ChatGroq(model="gemini-1.5-flash")

#now its embeddings model
embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")






