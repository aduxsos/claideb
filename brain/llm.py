from ollama import chat

MODEL_NAME = "qwen3:8b"

messages = [
    {
        "role": "system",
        "content": """
        You are Claideb.

        You are Matt's personal AI assistant.

        You run locally on Matt's computer.

        You are concise, intelligent, and practical.

        Never say you are Qwen or another AI model unless Matt specifically asks about your underlying model.

        When someone asks who you are, introduce yourself as Claideb.
        """
    }
]


def ask(user_message):

    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    response = chat(
        model=MODEL_NAME,
        messages=messages
    )

    assistant_reply = response.message.content

    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    return assistant_reply