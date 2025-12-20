import json
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
