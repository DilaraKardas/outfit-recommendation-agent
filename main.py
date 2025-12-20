import json
print("agent started")

with open("clothes.json", "r", encoding= "utf-8") as file:
    clothes = json.load(file)

    print("Number of clothes in wardrobe:", len(clothes))
    for item in clothes:
        print("- ", item["name"])