import os
import streamlit as st

from dotenv import load_dotenv
from tavily import TavilyClient
from langchain_groq import ChatGroq

# Load .env for local execution
load_dotenv()


def get_secret(key):
    """
    Works for BOTH:
    1. Local (.env)
    2. Streamlit Cloud (Secrets)
    """
    try:
        return st.secrets[key]
    except Exception:
        return os.getenv(key)


GROQ_API_KEY = get_secret("GROQ_API_KEY")
TAVILY_API_KEY = get_secret("TAVILY_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY not found")


client = TavilyClient(
    api_key=TAVILY_API_KEY
)

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0
)


def search_web(question):

    results = client.search(
        query=question,
        max_results=5
    )

    context = ""
    sources = []

    for item in results["results"]:
        context += item["content"] + "\n\n"
        sources.append(item["url"])

    prompt = f"""
You are an AI assistant.

Answer the user's question ONLY using the information below.

Context:
{context}

Question:
{question}

If the answer is not available in the context, say:
"I couldn't find reliable information."

Answer:
"""

    response = llm.invoke(prompt)

    return response.content, sources
