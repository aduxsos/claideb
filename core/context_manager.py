MAX_CONTEXT_TOKENS = 6000
CHARS_PER_TOKEN = 3.5


def estimate_tokens(message):

    content = message.get("content", "")

    estimated_tokens = len(content) / CHARS_PER_TOKEN

    return int(estimated_tokens) + 4


def build_context(messages, system_message):

    context = [system_message]

    used_tokens = estimate_tokens(system_message)

    recent_messages = []

    for message in reversed(messages[1:]):

        message_tokens = estimate_tokens(message)

        if used_tokens + message_tokens > MAX_CONTEXT_TOKENS:

            if not recent_messages:
                recent_messages.append(message)

            break

        recent_messages.append(message)
        used_tokens += message_tokens

    recent_messages.reverse()

    context.extend(recent_messages)
    return context
    
def estimate_context_tokens(context):

    total_tokens = 0

    for message in context:
        total_tokens += estimate_tokens(message)

    return total_tokens


def get_context_stats(context):

    return {
        "messages": len(context) - 1,
        "estimated_tokens": estimate_context_tokens(context),
        "max_tokens": MAX_CONTEXT_TOKENS
    }
