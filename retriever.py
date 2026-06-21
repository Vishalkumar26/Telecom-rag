"""Merged retriever: queries FAQ, Tickets, and Guides stores in parallel."""

from pathlib import Path
from typing import List

from langchain_core.callbacks import CallbackManagerForRetrieverRun
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever

from embeddings import FastEmbedEmbeddings
from vectorstore import NumpyVectorStore

STORE_DIR = Path(__file__).parent / "faiss_store"
COLLECTIONS = ["faq", "tickets", "guides", "plans"]
TOP_K = 3  # per collection → 12 total


def get_embeddings():
    return FastEmbedEmbeddings()


class MergedRetriever(BaseRetriever):
    """Retriever that merges results from multiple NumpyVectorStores."""

    stores: List[NumpyVectorStore]
    k: int = 3

    class Config:
        arbitrary_types_allowed = True

    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        docs = []
        for store in self.stores:
            docs.extend(store.similarity_search(query, k=self.k))
        return docs


def get_retriever():
    """Return a MergedRetriever that fetches top-3 from each collection."""
    embeddings = get_embeddings()

    stores = []
    for name in COLLECTIONS:
        store_path = STORE_DIR / name
        store = NumpyVectorStore.load_local(str(store_path), embeddings)
        stores.append(store)

    return MergedRetriever(stores=stores, k=TOP_K)
