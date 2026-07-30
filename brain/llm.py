from ollama import chat

MODEL_NAME = "qwen3:8b"


def ask(user_message):
    response = chat(
        model=MODEL_NAME,
       messages=[
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
           },
           {
               "role": "user",
               "content": user_message
           }
           ]
    )
    
       

    return response.message.content