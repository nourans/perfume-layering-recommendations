from openai import OpenAI
import app.py
import os
from .env import load_dotenv
"""https://platform.openai.com/docs/guides/structured-outputs?api-mode=responses
 to output structured data if needed... using this if i want to get json outputs for
 top, mid, base notes
 
 
 what we put in the .env file are called environment variables"""



load_dotenv()
client = OpenAI(
    apikey = os.getenv("OPENAI_API_KEY")
)
perfumes = load_perfumes()

def load_perfumes():
    with open(DATA_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

response = client.responses.create(
    model = "gpt=4o",
    tools=[{"type": "web_search_preview"}],
    input = f"These are my perfumes: {perfumes}. tell me the top 5 most common notes 
    among my perfumes then the top 5 most common note combinations in each 
    perfume and where do they occur so I can better understand the what notes in 
    perfumes attract me the most. "
)


