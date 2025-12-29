import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'logic'))
import json
import random
from logic.filters import hard_filter
from logic.outfit_engine import group_by_category, build_outfit, print_outfit 


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


    grouped_items = group_by_category(filtered_items)
    outfit = build_outfit(grouped_items, user_input["weather"])
    print_outfit(outfit)
