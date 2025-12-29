import json
import os

def load_items():
    base_dir = os.path.dirname(__file__) 
    file_path = os.path.join(base_dir, "clothes.json")

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
