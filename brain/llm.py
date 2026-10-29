from ollama import chat
from memory.chat_memory import save_messages, load_messages

MODEL_NAME = "gpt-oss:20b-cloud"
MAX_CONTEXT_MESSAGES = 12

SYSTEM_MESSAGE = {
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
    
loaded_messages = load_messages()

if loaded_messages is None:
    messages = [SYSTEM_MESSAGE]
else:
    messages = loaded_messages

def ask(user_message):

    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    system_message = messages[0]
    recent_messages = messages[1:][-MAX_CONTEXT_MESSAGES:]

    context = [system_message] + recent_messages

    response = chat(
        model=MODEL_NAME,
        messages=context
    )

    assistant_reply = response.message.content

    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )
    save_messages(messages)

    return assistant_reply