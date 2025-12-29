import json
from logic.filters import hard_filter
from logic.outfit_engine import group_by_category, build_outfit, print_outfit 
from services.weather_service import get_weather_by_city
from data.loader import load_items

city = input("Enter your city: ").strip()
mood = input("How are you feeling today? ").strip().lower()
occasion = input("What is the occasion? ").strip().lower()
style = input("Preferred style: ").strip().lower()

weather = get_weather_by_city(city)


print(f"Weather info: {weather}")

items = load_items()

user_input = {
        "weather": weather,
        "occasion": occasion,
        "style": style,
        "season": "all"  # şimdilik sabit
    }

filtered_items = hard_filter(items, user_input)

grouped = group_by_category(filtered_items)
outfit = build_outfit(grouped, weather)

print_outfit(outfit)