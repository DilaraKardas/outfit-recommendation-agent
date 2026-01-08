def score_item(item, user_input):
    score = 0

    if user_input["style"] in item["style"]:
        score += 3

    if user_input["occasion"] in item["occasion"]:
        score += 3
    
    if user_input["weather"] in item["weather"] or "all" in item["weather"]:
        score += 2

    if user_input["season"] in item["season"] or "all" in item["season"]:
        score += 1

    if "mood" in item and user_input.get("mood") in item.get("mood", []):
        score += 1

    return score


def select_best_items(items, user_input):
    
    print("\n--- ITEMS ENTERING select_best_items ---")
    for item in items:
        print(item["name"], item["layer"])

    best_by_category = {}
    #her kıyafet için kategori ve skor bilgisi belirleniyor 
    for item in items:
        category = item["category"]
        item_score = score_item(item, user_input)

        if category not in best_by_category: #eğer o kategori sözlükte yoksa skoruyla birlikte sözlüğe eklenir
            best_by_category[category] = (item, item_score)
        else:
            _, current_score = best_by_category[category] #eğer sözlükte varsa var olan kategorinin skoruyla karşılaştırılır. skoru büyük olan sözlüğe eklenir
            if item_score > current_score:
                best_by_category[category] = (item, item_score)

    return {category: data[0] for category, data in best_by_category.items()}