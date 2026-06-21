"""LangChain LCEL chain: retriever → prompt → Groq LLM → streamed output."""

import os
from dotenv import load_dotenv

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq

from retriever import get_retriever

load_dotenv()

SYSTEM_PROMPT = """\
You are a helpful telecom customer support assistant for NovaCell.

RULES:
1. Answer the customer's question using ONLY the retrieved context below.
2. Do NOT use any knowledge outside of the provided context.
3. If the context does not contain enough information to answer, say:
   "I don't have enough information to answer that. Please call 611 or use the MyTelecom app for further assistance."
4. Be concise, friendly, and professional.
5. When listing steps, use numbered lists.
6. Always cite which source type the information came from (FAQ, TICKETS, or GUIDES) when relevant.

RETRIEVED CONTEXT:
{context}
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("human", "{question}"),
    ]
)


def format_docs(docs):
    """Format retrieved documents with source labels."""
    formatted = []
    for doc in docs:
        source = doc.metadata.get("source", "UNKNOWN")
        formatted.append(f"[{source}] {doc.page_content}")
    return "\n\n---\n\n".join(formatted)


def get_chain():
    """Build and return the RAG chain."""
    retriever = get_retriever()

    llm = ChatGroq(
        model="qwen/qwen3-32b",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY"),
    )

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
