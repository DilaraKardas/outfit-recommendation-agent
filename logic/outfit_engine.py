from collections import defaultdict

def group_by_category(items):
  
    grouped = defaultdict(list)

    for item in items:
        grouped[item["category"]].append(item)

    return grouped


def build_outfit(grouped_items, weather):

    # şimdilik ilk uygun olanı seçiyor
    outfit = {}
    outfit["top"] = grouped_items.get("top", [None])[0]
    outfit["bottom"] = grouped_items.get("bottom", [None])[0]
    outfit["footwear"] = grouped_items.get("footwear", [None])[0]

    if weather in ["cold", "cool"]:
        outfit["outerwear"] = grouped_items.get("outerwear", [None])[0]

    outfit["bag"] = grouped_items.get("bag", [None])[0]

    return outfit


def print_outfit(outfit):
    print("\nRecommended Outfit:\n")

    for part, item in outfit.items():
        if item:
            print(f"- {part.capitalize()}: {item['name']}")
