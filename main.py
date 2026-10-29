from brain.llm import ask

print("=== Claideb v0.0.3 ===")
print("Commands: /multi, exit")
print("Type /multi to enter a multiline message.\n")


while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("Claideb: Goodbye!")
        break

    if user_message.lower() == "/multi":
        print("Claideb: Multiline mode. Type /end on a new line to send.")
        print("Type /cancel on a new line to cancel.\n")

        lines = []

        while True:
            line = input()

            if line.lower() == "/end":
                break

            if line.lower() == "/cancel":
                lines = []
                print("Claideb: Message cancelled.\n")
                break

            lines.append(line)

        if not lines:
            continue

        user_message = "\n".join(lines)

    answer = ask(user_message)

    print("\nClaideb:", answer)
    print()