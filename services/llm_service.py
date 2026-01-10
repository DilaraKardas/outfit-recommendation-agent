def generate_explanation_with_llm(client, item_name, rule_explanation, user_input):
    prompt = f"""You are a fashion assistant.

    User context:
    -Mood: {user_input['mood']}
    -Occasion: {user_input['occasion']}
    -Style: {user_input['style']}
    -Weather: {user_input['weather']}

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
    