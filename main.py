import json
import random
print("agent started")

with open("clothes.json", "r", encoding= "utf-8") as file:
    clothes = json.load(file)

    print("Wardrobe loaded...")
    print("Number of clothes in wardrobe:", len(clothes))
    
    user_mood = input("How are you feeling today? (e.g., happy, sad, energetic, relaxed): ").strip().lower()
    print("User mood received:", user_mood)

    #filter clothes based on mood
    matching_clothes = []

    for item in clothes:
        if user_mood in item["mood"]:
            matching_clothes.append(item)

    print("\nClothes matching your mood:\n")
    if len(matching_clothes) == 0:
        print("No matching clothes found.")
    else:
        for item in matching_clothes:
            print("-", item["name"], f"({item['category']})")


    # get weather condition
    weather_condition = input("What is the weather like today? (e.g., warm, cold, rainy): ").strip().lower()

    print("Mood:", user_mood)
    print("Weather:", weather_condition)

    # filter clothes based on weather

    for item in clothes:
        mood_match = user_mood in item["mood"]
        weather_match = (item["weather"] == "all" or item["weather"] == weather_condition) #hava durumuna göre özel kıyafet önerilir, havaya özel kıyafet yoksa genel olanlardan önerilir 

        if mood_match and weather_match:
            matching_clothes.append(item)

    #seperate by category
    tops = [item for item in matching_clothes if item["category"] == "top"]
    bottoms = [item for item in matching_clothes if item["category"] == "bottom"]

    #recommennd outfit

    print("\nOutfit recommendation:")

    if not tops or not bottoms:
        print("Not enaugh matching clothes to create a full outfit")
    else:
        selected_top = random.choice(tops) #şimdilik random, sonra zeka yüklenecek
        selected_bottom = random.choice(bottoms)

        print("Top :", selected_top["name"])
        print("Bottom :", selected_bottom["name"])

 
             
            
