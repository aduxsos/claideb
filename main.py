from brain.llm import ask

print("=== Claideb v0.0.2 ===")
print("Type 'exit' to quit.\n")

while True:

    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("Claideb: Goodbye!")
        break

    answer = ask(user_message)

    print("Claideb:", answer)
    print()