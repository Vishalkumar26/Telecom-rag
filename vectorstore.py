"""Simple numpy-based vector store with cosine similarity search and pickle persistence."""

import pickle
from pathlib import Path
from typing import List, Optional

import numpy as np
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import VectorStore


class NumpyVectorStore(VectorStore):
    """A minimal vector store backed by numpy arrays and pickle persistence."""

    def __init__(self, embedding: Embeddings, store_path: Optional[str] = None):
        self._embedding = embedding
        self._store_path = Path(store_path) if store_path else None
        self._documents: List[Document] = []
        self._vectors: Optional[np.ndarray] = None

    @property
    def embeddings(self) -> Embeddings:
        return self._embedding

    def add_documents(self, documents: List[Document], **kwargs) -> List[str]:
        texts = [doc.page_content for doc in documents]
        vectors = self._embedding.embed_documents(texts)
        new_vectors = np.array(vectors, dtype=np.float32)

        if self._vectors is not None:
            self._vectors = np.vstack([self._vectors, new_vectors])
        else:
            self._vectors = new_vectors

        self._documents.extend(documents)
        return [str(i) for i in range(len(self._documents) - len(documents), len(self._documents))]

    def add_texts(self, texts, metadatas=None, **kwargs):
        docs = []
        for i, text in enumerate(texts):
            meta = metadatas[i] if metadatas else {}
            docs.append(Document(page_content=text, metadata=meta))
        return self.add_documents(docs)

    def similarity_search(self, query: str, k: int = 4, **kwargs) -> List[Document]:
        if self._vectors is None or len(self._documents) == 0:
            return []

        query_vector = np.array(self._embedding.embed_query(query), dtype=np.float32)

        # Cosine similarity
        norms = np.linalg.norm(self._vectors, axis=1)
        query_norm = np.linalg.norm(query_vector)

        # Avoid division by zero
        safe_norms = np.where(norms == 0, 1, norms)
        safe_query_norm = query_norm if query_norm != 0 else 1

        similarities = (self._vectors @ query_vector) / (safe_norms * safe_query_norm)

        # Get top-k indices
        top_k = min(k, len(self._documents))
        top_indices = np.argsort(similarities)[-top_k:][::-1]

        return [self._documents[i] for i in top_indices]

    def save_local(self, path: str) -> None:
        """Persist the store to disk."""
        store_path = Path(path)
        store_path.mkdir(parents=True, exist_ok=True)
        data = {
            "documents": self._documents,
            "vectors": self._vectors,
        }
        with open(store_path / "store.pkl", "wb") as f:
            pickle.dump(data, f)

    @classmethod
    def load_local(cls, path: str, embedding: Embeddings) -> "NumpyVectorStore":
        """Load a persisted store from disk."""
        store_path = Path(path)
        with open(store_path / "store.pkl", "rb") as f:
            data = pickle.load(f)

        store = cls(embedding=embedding, store_path=path)
        store._documents = data["documents"]
        store._vectors = data["vectors"]
        return store

    @classmethod
    def from_documents(cls, documents: List[Document], embedding: Embeddings, **kwargs) -> "NumpyVectorStore":
        store = cls(embedding=embedding)
        store.add_documents(documents)
        return store

    @classmethod
    def from_texts(cls, texts: List[str], embedding: Embeddings, metadatas=None, **kwargs) -> "NumpyVectorStore":
        docs = []
        for i, text in enumerate(texts):
            meta = metadatas[i] if metadatas else {}
            docs.append(Document(page_content=text, metadata=meta))
        return cls.from_documents(docs, embedding)
