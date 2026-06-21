"""Ingest resolved support tickets from data/tickets.db into FAISS vector store."""

import sqlite3
from pathlib import Path

from langchain_core.documents import Document
from embeddings import FastEmbedEmbeddings
from vectorstore import NumpyVectorStore

STORE_DIR = Path(__file__).parent / "faiss_store" / "tickets"
DB_PATH = Path(__file__).parent / "data" / "tickets.db"


def ingest_tickets():
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"{DB_PATH} not found. Run 'python seed_tickets.py' first."
        )

    embeddings = FastEmbedEmbeddings()

    # Idempotent: skip if already exists
    if (STORE_DIR / "store.pkl").exists():
        print(f"Store already exists at {STORE_DIR} — skipping.")
        return NumpyVectorStore.load_local(str(STORE_DIR), embeddings)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, category, resolution FROM tickets")
    rows = cur.fetchall()
    conn.close()

    docs = []
    for ticket_id, category, resolution in rows:
        docs.append(
            Document(
                page_content=resolution,
                metadata={
                    "source": "TICKETS",
                    "category": category,
                    "ticket_id": str(ticket_id),
                },
            )
        )

    store = NumpyVectorStore.from_documents(docs, embeddings)
    store.save_local(str(STORE_DIR))
    print(f"Ingested {len(docs)} tickets into {STORE_DIR}.")
    return store


if __name__ == "__main__":
    ingest_tickets()
