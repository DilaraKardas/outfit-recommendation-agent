def generate_explanation_with_llm(client, item_name, rule_explanation, user_input):
    prompt = f"""You are a fashion assistant.

    User context:
    -Mood: {user_input['mood']}
    -Occasion: {user_input['occasion']}
    -Style: {user_input['style']}
    -Weather: {user_input.get('weather', 'bilinmiyor')}
    Item selected: {item_name}

    Technical reasoning (the "Why"):
    {rule_explanation}

    TASK: Explain to the user in a friendly, supportive, and natural way why this specific item was chosen for them. 
    Keep it concise (max 2-3 sentences). Answer in Turkish.
    """

    try:
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"This item was selected because {rule_explanation.lower()}." 
    

def generate_llm_explanation(outfit, user_input, client):
    """
    OUTFIT-BAZLI AÇIKLAMA (UI / Jüri sunumu için)
    """
    item_list = "\n".join(
        [f"- {category}: {item['item']['name']}" for category, item in outfit.items()]
    )

    prompt = f"""You are a professional AI fashion stylist.

    User context:
    - Mood: {user_input['mood']}
    - Occasion: {user_input['occasion']}
    - Style: {user_input['style']}
    - Weather: {user_input.get('weather', 'bilinmiyor')}

    Selected outfit:
    {item_list}

    TASK:
    Explain in a warm, confident and stylish tone why this outfit fits the user.
    Keep it short (2–3 sentences).
    Answer in Turkish.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception:
        return "Bu kombin, stil tercihleriniz ve günün koşulları göz önünde bulundurularak seçildi."
