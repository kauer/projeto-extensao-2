#!/usr/bin/env python3
"""
Minimal LangGraph + LangChain RAG (single file)

Prereqs (one-time):
  pip install -U langchain langchain-openai langgraph tiktoken

Env vars (example):
  export OPENAI_API_KEY="sk-..."                # required
  export OPENAI_BASE_URL="https://your.openai-compatible.endpoint/v1"  # optional
  export OPENAI_MODEL="gpt-4o-mini"            # optional (chat model)
  export OPENAI_EMBEDDING_MODEL="text-embedding-3-small"  # optional (embedding model)

Run:
  python rag_langgraph_basic.py
"""

import os
from dotenv import load_dotenv
load_dotenv()
from typing import List, TypedDict

from langgraph.graph import StateGraph, START, END  # Graph orchestration
from langchain_openai import ChatOpenAI, OpenAIEmbeddings  # OpenAI-compatible chat + embeddings
from langchain_core.documents import Document  # LangChain document container
from langchain_core.vectorstores import InMemoryVectorStore  # In-memory vector store
from langchain_core.prompts import ChatPromptTemplate  # Prompt building for chat models


# -----------------------------
# Configuration from environment
# -----------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")  # Optional: for OpenAI-compatible providers
CHAT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
EMBED_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is required")


# -----------------------------
# LLM and Embeddings
# -----------------------------
llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,  # works with OpenAI-compatible providers
    model=CHAT_MODEL,
    temperature=0.2,
)

embeddings = OpenAIEmbeddings(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,  # works with OpenAI-compatible providers
    model=EMBED_MODEL,
)

# -----------------------------
# Mock corpus (replace as needed)
# -----------------------------
MOCK_TEXTS = [
    "LangGraph is a graph-based orchestration library for building stateful, multi-step LLM workflows.",
    "Retrieval Augmented Generation (RAG) combines a retriever over external data with a generator LLM.",
    "An in-memory vector store is convenient for prototyping; switch to a persistent vector DB in production.",
    "LangChain provides standardized interfaces for models, prompts, retrievers, and vector stores.",
]

docs: List[Document] = [
    Document(page_content=text, metadata={"source": f"mock:{i}"}) for i, text in enumerate(MOCK_TEXTS)
]

# -----------------------------
# Minimal in-memory retriever
# -----------------------------
vector_store = InMemoryVectorStore(embedding=embeddings)
vector_store.add_documents(documents=docs, ids=[f"doc-{i}" for i in range(len(docs))])
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# -----------------------------
# Prompt for generation
# -----------------------------
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that answers strictly using the provided context. "
            "If the answer is not in the context, say you don't know.",
        ),
        (
            "human",
            "Question:\n{question}\n\nContext:\n{context}\n\nAnswer in 1-3 sentences.",
        ),
    ]
)

# -----------------------------
# Graph state and nodes
# -----------------------------
class RAGState(TypedDict):
    question: str
    documents: List[Document]
    answer: str

def retrieve_node(state: RAGState) -> dict:
    question = state["question"]
    retrieved = retriever.invoke(question)
    return {"documents": retrieved}

def generate_node(state: RAGState) -> dict:
    # Concatenate retrieved docs into a single context string
    context_blocks = [f"- {d.page_content}" for d in state["documents"]]
    context = "\n".join(context_blocks) if context_blocks else "(no context found)"

    # Build messages via prompt, then invoke chat model
    messages = prompt.invoke({"question": state["question"], "context": context})
    ai_msg = llm.invoke(messages)
    return {"answer": ai_msg.content}

# -----------------------------
# Build and compile the graph
# -----------------------------
graph = StateGraph(RAGState)
graph.add_node("retrieve", retrieve_node)
graph.add_node("generate", generate_node)

graph.add_edge(START, "retrieve")
graph.add_edge("retrieve", "generate")
graph.add_edge("generate", END)

app = graph.compile()


# -----------------------------
# Simple CLI runner
# -----------------------------
def run_query(question: str) -> str:
    initial: RAGState = {"question": question, "documents": [], "answer": ""}
    final_state = app.invoke(initial)
    return final_state["answer"]

if __name__ == "__main__":
    print("Minimal LangGraph RAG. Type a question (Ctrl+C to exit).")
    while True:
        try:
            q = input("\nQ> ").strip()
            if not q:
                continue
            print("A>", run_query(q))
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break
