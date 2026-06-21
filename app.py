"""Streamlit UI for the RAG Telecom Customer Care Chatbot."""

import streamlit as st
from chain import get_chain

st.set_page_config(page_title="TeleCom Support", page_icon="📱", layout="wide")

# ── Sidebar ──────────────────────────────────────────────────────────────────

SAMPLE_QUESTIONS = [
    "Why is my mobile internet so slow?",
    "How do I activate international roaming?",
    "What are the roaming charges in the EU?",
    "How do I replace a lost SIM card?",
    "Why is my bill higher than usual?",
    "How do I enable Wi-Fi calling?",
    "How do I set up autopay?",
    "My phone shows SIM not detected. What should I do?",
]

with st.sidebar:
    st.header("Sample Questions")
    st.caption("Click any question to send it instantly.")
    for q in SAMPLE_QUESTIONS:
        if st.button(q, key=q, use_container_width=True):
            st.session_state["pending_question"] = q

    st.divider()
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state["messages"] = []
        st.session_state.pop("pending_question", None)
        st.rerun()

# ── Main chat area ───────────────────────────────────────────────────────────

st.title("📱 TeleCom Support Chatbot")
st.caption("Powered by RAG — answers grounded in FAQ, resolved tickets, guides, and plans for TeleCom.")

# Initialise session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Determine input source: sidebar click or chat input
user_input = st.chat_input("Ask a question about your telecom service…")

if "pending_question" in st.session_state:
    user_input = st.session_state.pop("pending_question")

if user_input:
    # Show user message
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Stream assistant response
    chain = get_chain()
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        for chunk in chain.stream(user_input):
            full_response += chunk
            placeholder.markdown(full_response + "▌")
        placeholder.markdown(full_response)

    st.session_state["messages"].append({"role": "assistant", "content": full_response})
