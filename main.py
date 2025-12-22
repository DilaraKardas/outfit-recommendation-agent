import json
import random
from logic.filters import hard_filter

with open("data/clothes.json", "r", encoding= "utf-8") as file:
    clothes = json.load(file)


    user_input = {
        "mood": "happy",
        "weather": "warm", 
        "season": "summer",
        "occasion": "hangout",
        "style": "casual" 
    }

    filtered_items = hard_filter(clothes, user_input)
    print("filtered items: ")

    for item in filtered_items:
        print("-", item["name"], f"({item['category']})")


    

