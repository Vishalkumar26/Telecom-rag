"""CLI REPL interface for the RAG Telecom Chatbot."""

from chain import get_chain


def main():
    print("=" * 60)
    print("  NovaCell Telecom Support Chatbot (CLI)")
    print("  Type your question and press Enter.")
    print("  Type 'quit' to exit.")
    print("=" * 60)
    print()

    chain = get_chain()

    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not question:
            continue
        if question.lower() == "quit":
            print("Goodbye!")
            break

        print("Bot: ", end="", flush=True)
        for chunk in chain.stream(question):
            print(chunk, end="", flush=True)
        print("\n")


if __name__ == "__main__":
    main()
