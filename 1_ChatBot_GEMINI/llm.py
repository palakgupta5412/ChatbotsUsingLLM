from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_llm(conversation, config):

    prompt = ""

    for msg in conversation:
        prompt += f"{msg['role']}: {msg['content']}\n"

    response = client.models.generate_content(
        model=config["model"],
        contents=prompt
    )

    return response.text