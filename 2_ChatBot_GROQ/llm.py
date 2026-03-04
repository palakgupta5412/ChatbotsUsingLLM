from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(conversation, config):

    response = client.chat.completions.create(
        model=config["model"],
        messages=conversation
    )

    return response.choices[0].message.content