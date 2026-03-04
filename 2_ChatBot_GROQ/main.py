import json
from file import getChat, addChat
from llm import ask_llm

with open("./config.json") as f:
    config = json.load(f)

conversation = getChat()

if not conversation:
    conversation.append({
        "role": "system",
        "content": config["system_prompt"]
    })

print("Commands: /clear /help /exit\n")

while True:

    user_input = input("You: ")

    if user_input == "/exit":
        break

    if user_input == "/clear":
        conversation = []
        conversation.append({
            "role": "system",
            "content": config["system_prompt"]
        })
        print("Chat cleared")
        continue

    if user_input == "/help":
        print("/clear → reset chat")
        print("/exit → quit")
        continue

    conversation.append({
        "role": "user",
        "content": user_input
    })

    try:

        reply = ask_llm(conversation, config)

        print("El:", reply)

        conversation.append({
            "role": "assistant",
            "content": reply
        })

        addChat(conversation)

    except Exception as e:
        print("Error:", e)