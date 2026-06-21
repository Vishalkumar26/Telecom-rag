"""Custom embedding wrapper using FastEmbed (ONNX-based, no PyTorch required)."""

from typing import List

from langchain_core.embeddings import Embeddings
from fastembed import TextEmbedding


class FastEmbedEmbeddings(Embeddings):
    """LangChain-compatible embedding class backed by FastEmbed (ONNX)."""

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self._model = TextEmbedding(model_name)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [emb.tolist() for emb in self._model.embed(texts)]

    def embed_query(self, text: str) -> List[float]:
        return list(self._model.embed([text])).__iter__().__next__().tolist()
