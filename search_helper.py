import os

from dotenv import load_dotenv
from tavily import TavilyClient
from langchain_groq import ChatGroq

load_dotenv()

# Initialize Tavily Client
client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

# Initialize Groq
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
    temperature=0
)


def search_web(question):

    # Search the web
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

Answer the question only using the following context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content, sources