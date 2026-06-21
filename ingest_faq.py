"""Ingest FAQ entries from data/faq.csv into FAISS vector store."""

import csv
from pathlib import Path

from langchain_core.documents import Document
from embeddings import FastEmbedEmbeddings
from vectorstore import NumpyVectorStore

STORE_DIR = Path(__file__).parent / "faiss_store" / "faq"
FAQ_PATH = Path(__file__).parent / "data" / "faq.csv"


def ingest_faq():
    embeddings = FastEmbedEmbeddings()

    # Idempotent: skip if already exists
    if (STORE_DIR / "store.pkl").exists():
        print(f"Store already exists at {STORE_DIR} — skipping.")
        return NumpyVectorStore.load_local(str(STORE_DIR), embeddings)

    docs = []
    with open(FAQ_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            content = f"Q: {row['question']}\nA: {row['answer']}"
            docs.append(
                Document(
                    page_content=content,
                    metadata={
                        "source": "FAQ",
                        "category": row.get("category", ""),
                        "id": row.get("id", ""),
                    },
                )
            )

    store = NumpyVectorStore.from_documents(docs, embeddings)
    store.save_local(str(STORE_DIR))
    print(f"Ingested {len(docs)} FAQ entries into {STORE_DIR}.")
    return store


if __name__ == "__main__":
    ingest_faq()
