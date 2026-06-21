"""Ingest PDF telecom guide chunks into FAISS vector store."""

from pathlib import Path

from langchain_core.documents import Document
from embeddings import FastEmbedEmbeddings
from vectorstore import NumpyVectorStore
from pypdf import PdfReader

STORE_DIR = Path(__file__).parent / "faiss_store" / "guides"
PDF_PATH = Path(__file__).parent / "data" / "telecom_guide.pdf"

CHUNK_SIZE = 600
CHUNK_OVERLAP = 100


def _split_text(text: str, chunk_size: int, overlap: int) -> list:
    """Split text into overlapping chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks


def ingest_guides():
    if not PDF_PATH.exists():
        raise FileNotFoundError(
            f"{PDF_PATH} not found. Run 'python generate_guide_pdf.py' first."
        )

    embeddings = FastEmbedEmbeddings()

    # Idempotent: skip if already exists
    if (STORE_DIR / "store.pkl").exists():
        print(f"Store already exists at {STORE_DIR} — skipping.")
        return NumpyVectorStore.load_local(str(STORE_DIR), embeddings)

    # Extract text from PDF
    reader = PdfReader(str(PDF_PATH))
    full_text = "\n".join(page.extract_text() or "" for page in reader.pages)

    # Chunk the text using simple recursive splitting
    chunks = _split_text(full_text, CHUNK_SIZE, CHUNK_OVERLAP)

    docs = [
        Document(
            page_content=chunk,
            metadata={"source": "GUIDES", "chunk_index": i},
        )
        for i, chunk in enumerate(chunks)
    ]

    store = NumpyVectorStore.from_documents(docs, embeddings)
    store.save_local(str(STORE_DIR))
    print(f"Ingested {len(docs)} guide chunks into {STORE_DIR}.")
    return store


if __name__ == "__main__":
    ingest_guides()
