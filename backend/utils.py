"""core utility functions — loading & saving data"""
import os
import json

DATA_PATH = "data/perfume_input.json"

def load_perfumes():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_perfumes(perfumes):
    with open(DATA_PATH, "w") as file:
        json.dump(perfumes, file, indent=4)