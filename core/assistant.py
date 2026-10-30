from brain.llm import generate_response, SYSTEM_MESSAGE
from memory.chat_memory import save_messages, load_messages
from core.context_manager import build_context, get_context_stats



loaded_messages = load_messages()

if loaded_messages is None:
    messages = [SYSTEM_MESSAGE.copy()]
else:
    messages = [SYSTEM_MESSAGE.copy()] + [
    message for message in loaded_messages
    if message.get("role") !="system"
    ]
def send_message(user_message):

    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    context = build_context(messages, SYSTEM_MESSAGE)
    stats = get_context_stats(context)
    print(f"\n[Context] Messages: {stats['messages']} | "
    f"Estimated tokens: {stats['estimated_tokens']} / "
    f"{stats['max_tokens']}"
    )
    

    try:
        assistant_reply = generate_response(context)

    except Exception as error:
        messages.pop()
        print(f"Claideb Error: {error}")
        return None

    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    save_messages(messages)

    return assistant_reply