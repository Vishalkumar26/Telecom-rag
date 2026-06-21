"""Ingest plan data from data/plans.json into the vector store."""

import json
from pathlib import Path

from langchain_core.documents import Document
from embeddings import FastEmbedEmbeddings
from vectorstore import NumpyVectorStore

STORE_DIR = Path(__file__).parent / "faiss_store" / "plans"
PLANS_PATH = Path(__file__).parent / "data" / "plans.json"


def _format_plan(plan: dict) -> str:
    """Convert a plan dict into a readable text document for embedding."""
    lines = [f"Plan: {plan['name']} ({plan.get('type', 'plan')})"]

    if "monthly_price" in plan:
        lines.append(f"Price: ${plan['monthly_price']}/month")
    elif "price" in plan:
        lines.append(f"Price: ${plan['price']} {plan.get('price_unit', '')}")

    if plan.get("data_unlimited"):
        lines.append("Data: Unlimited")
    elif plan.get("data_gb"):
        lines.append(f"Data: {plan['data_gb']} GB")

    if plan.get("talk_minutes"):
        lines.append(f"Talk: {plan['talk_minutes']}")
    if plan.get("texts"):
        lines.append(f"Texts: {plan['texts']}")
    if plan.get("hotspot_gb"):
        lines.append(f"Hotspot: {plan['hotspot_gb']} GB")
    if plan.get("network"):
        lines.append(f"Network: {plan['network']}")
    if plan.get("contract"):
        lines.append(f"Contract: {plan['contract']}")
    if plan.get("lines_included"):
        lines.append(f"Lines included: {plan['lines_included']}")
    if plan.get("price_per_line"):
        lines.append(f"Price per line: ${plan['price_per_line']}")
    if plan.get("coverage"):
        lines.append(f"Coverage: {plan['coverage']}")
    if plan.get("eligibility"):
        lines.append(f"Eligibility: {plan['eligibility']}")
    if plan.get("intro_offer"):
        lines.append(f"Intro offer: {plan['intro_offer']}")
    if plan.get("features"):
        lines.append("Features: " + "; ".join(plan["features"]))
    if plan.get("best_for"):
        lines.append(f"Best for: {plan['best_for']}")

    return "\n".join(lines)


def ingest_plans():
    if not PLANS_PATH.exists():
        raise FileNotFoundError(f"{PLANS_PATH} not found.")

    embeddings = FastEmbedEmbeddings()

    # Idempotent: skip if already exists
    if (STORE_DIR / "store.pkl").exists():
        print(f"Store already exists at {STORE_DIR} — skipping.")
        return NumpyVectorStore.load_local(str(STORE_DIR), embeddings)

    with open(PLANS_PATH, encoding="utf-8") as f:
        data = json.load(f)

    plans = data.get("plans", [])
    docs = []
    for plan in plans:
        content = _format_plan(plan)
        docs.append(
            Document(
                page_content=content,
                metadata={
                    "source": "PLANS",
                    "plan_id": plan.get("id", ""),
                    "category": plan.get("category", ""),
                    "type": plan.get("type", ""),
                },
            )
        )

    store = NumpyVectorStore.from_documents(docs, embeddings)
    store.save_local(str(STORE_DIR))
    print(f"Ingested {len(docs)} plans into {STORE_DIR}.")
    return store


if __name__ == "__main__":
    ingest_plans()
