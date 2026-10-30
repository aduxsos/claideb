import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEMORY_FILE = os.path.join(BASE_DIR, "conversation.json")
TEMP_FILE = os.path.join(BASE_DIR, "conversation.tmp")

def save_messages(messages):

    try:
        with open(TEMP_FILE, "w", encoding="utf-8") as file:
            json.dump(messages, file, indent=4, ensure_ascii=False)

        os.replace(TEMP_FILE, MEMORY_FILE)
        
        except OSError as error:
    print(f"Memory Save Error: {error}")

    try:
        if os.path.exists(TEMP_FILE):
            os.remove(TEMP_FILE)

    except OSError as cleanup_error:
        print(f"Memory Cleanup Error: {cleanup_error}")

        
def load_messages():
    if not os.path.exists(MEMORY_FILE):
        return None

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            messages = json.load(file)

    except json.JSONDecodeError:
        print("Memory Error: conversation.json is corrupted.")
        return None


    if not isinstance(messages, list):
        print("Memory Error: Invalid conversation structure.")
        return None

    for message in messages:
        if not isinstance(message, dict):
            print("Memory Error: Invalid message format.")
            return None

        if not isinstance(message.get("role"), str):
            print("Memory Error: Missing or invalid message role.")
            return None

        if not isinstance(message.get("content"), str):
            print("Memory Error: Missing or invalid message content.")
            return None

    return messages