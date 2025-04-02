import os
import json
from openai import OpenAI
from utils import load_perfumes
from dotenv import load_dotenv
"""https://platform.openai.com/docs/guides/structured-outputs?api-mode=responses
 to output structured data if needed... using this if i want to get json outputs for
 top, mid, base notes
 
 fyi: what we put in the .env file are called environment variables"""

load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

def get_layering_recs():
    perfumes = load_perfumes()
    prompt = (f"""These are my perfumes: {perfumes}. based on top, middle, and base notes 
    for each one and on perfume layering principles, tell me which combinations I should 
    do to layer these perfumes so that they are the most complimentary. in what order? 
    tell me a super brief sentence for why you selected these combinations. then when 
    you're done, tell me the top 5 most common notes among my perfumes then the top 5 
    most common note combinations in each perfume and where do they occur so I can better 
    understand the what notes in perfumes attract me the most. make this whole answer as 
    brief and concise as possible. the most important thing is that before you give the 
    perfume taste analysis (i.e. the top 5 notes and the top 5 note combinations), 
    you must print "Taste Analysis".""")


    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# trial = get_layering_recs()
# print(trial)