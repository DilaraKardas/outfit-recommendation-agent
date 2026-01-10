import json
from logic.filters import hard_filter
from logic.outfit_engine import group_by_category, build_outfit, print_outfit 
from logic.scoring import select_best_items
from services.weather_service import get_weather_by_city
from data.loader import load_items
from logic.explain import explain_item
from google import genai



city = input("Enter your city: ").strip()
mood = input("How are you feeling today? ").strip().lower()
occasion = input("What is the occasion? ").strip().lower()
style = input("Preferred style: ").strip().lower()

weather = get_weather_by_city(city)


print(f"Weather info: {weather}")

user_input = {
        "weather": weather,
        "occasion": occasion,
        "style": style,
        "season": "all",  # şimdilik sabit
        "mood" : mood
    }

items = load_items()
filtered_items = hard_filter(items, user_input)

final_outfit = select_best_items(filtered_items, user_input)   
print("\n--- FINAL OUTFIT ---\n")
for category, item in final_outfit.items():
    print(f"{category.upper()}: {item['item']['name']}")

client = genai.Client()

for category, scored_item in final_outfit.items():
    print(f"{category.upper()}: {scored_item['item']['name']}")

    explanation = explain_item(
        scored_item = scored_item,
        user_input = user_input,
        client = client
    )

    print(f"Stil önerisi: {explanation}\n")

