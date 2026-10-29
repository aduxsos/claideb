import json
import os


def save_messages(messages):
    with open("conversation.json", "w", encoding="utf-8") as file:
        json.dump(messages, file, indent=4)


def load_messages():
    if os.path.exists("conversation.json"):
        with open("conversation.json", "r", encoding="utf-8") as file:
            messages = json.load(file)

        return messages

    else:
        return None