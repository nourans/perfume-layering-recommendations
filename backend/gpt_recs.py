"""Handles communication with the OpenAI API to generate perfume layering 
recommendations and analysis."""  
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
    prompt = (f"""
        These are my perfumes: {perfumes}. based on top, middle, and base notes 
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
        messages = [{"role": "user", "content": prompt}]) #, response_format="json")
        
    # json_str = response.choices[0].message.content
    # return json.loads(json_str)
    return response.choices[0].message.content

def parse_json_string(chatgpt_response):
    cleaned = chatgpt_response.strip().strip("```json").strip("```")
    try:
        parsed = json.loads(cleaned)
    except json.JSONDecodeError as e:
        print("⚠️ GPT did not return valid JSON. Here's the error:")
        print(e)
        print("\nHere's the raw response it gave:")
        print(cleaned)
        raise ValueError("Could not parse JSON")
    return parsed


def save_notes_to_file(notes_dict, filename="data/perfume_notes.json"):
    with open(filename, "w") as f:
        json.dump(notes_dict, f, indent=4)




# trial = get_layering_recs()
# print(trial)

"""These are my perfumes: {perfumes}. based on top, middle, and base notes 
    for each one and on perfume layering principles, tell me which combinations I should 
    do to layer these perfumes so that they are the most complimentary. in what order? 
    tell me a super brief sentence for why you selected these combinations. then when 
    you're done, tell me the top 5 most common notes among my perfumes then the top 5 
    most common note combinations in each perfume and where do they occur so I can better 
    understand the what notes in perfumes attract me the most. make this whole answer as 
    brief and concise as possible. the most important thing is that before you give the 
    perfume taste analysis (i.e. the top 5 notes and the top 5 note combinations), 
    you must print "Taste Analysis".
    
    floral = ["floral", "soft floral", "floral oriental", "soft oriental", "oriental", "woody oriental", "woody", "mossy wood", "dry wood", "aromatic", "citrus", "water", "green", "fruity"]
    
    """