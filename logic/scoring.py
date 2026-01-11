#scorelar katmanlandırılıyor
def base_match_score(item, user_input):
    score = 0
    explanation = []

    if user_input["style"] in item["style"]:
        score += 3
        explanation.append("style matches user preference (+3)")

    if user_input["occasion"] in item["occasion"]:
        score += 4
        explanation.append("occasion matches user need (+4)")

    return score, explanation

def formality_score(item, user_input):
    score = 0
    explanation = []

    if user_input["occasion"] in ["work", "meeting"]:
        if item.get("formality_level", 0) >= 4:
            score += 2
            explanation.append("high formality suitable for work/meeting (+2)")
        elif item.get("formality_level", 0) >= 2:
            score += 1
            explanation.append("acceptable formality for work/meeting (+1)")

    return score, explanation
    
def confidence_score(item, user_input):
    score = 0
    explanation = []

    # emotional support logic
    if user_input["mood"] in ["sad", "depressed", "anxious", "stressed"]:
        if item.get("confidence_boost", False) is True:
            score += 2
            explanation.append("confidence-boosting item for low mood (+2)")

    return score, explanation

def score_item(item, user_input):
    total_score = 0
    full_explanation = []

    base_score, base_exp = base_match_score(item, user_input)
    total_score += base_score
    full_explanation.extend(base_exp)

    formality_bonus, formality_exp = formality_score(item, user_input)
    total_score += formality_bonus
    full_explanation.extend(formality_exp)

    confidence_bonus, confidence_exp = confidence_score(item, user_input)
    total_score += confidence_bonus
    full_explanation.extend(confidence_exp)

    return{
        "item": item,
        "score": total_score,
        "explanation": full_explanation
    }

def select_best_items(items, user_input):
    
    print("\n--- ITEMS ENTERING select_best_items ---")
    for item in items:
        print(item["name"], item["layer"])

    best_by_category = {}
    #her kıyafet için kategori ve skor bilgisi belirleniyor 
    for item in items:
        scored = score_item(item, user_input)
        category = item["category"]
        
        if category not in best_by_category: #eğer o kategori sözlükte yoksa skoruyla birlikte sözlüğe eklenir
            best_by_category[category] = scored
        else: # varsa da var olanla skoru karşılaştırılıp yüksek olan sözlüğe eklenir
            if scored["score"] > best_by_category[category]["score"]:
                best_by_category[category] = scored

    return best_by_category