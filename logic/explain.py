def explain_item(scored_item):
    item =scored_item["item"]
    explanation = scored_item["explanation"]

    lines = []
    for exp in explanation:
        if "formality" in exp:
            lines.append("This piece is formal enough for the chosen occasion.")
        elif "style" in exp:
            lines.append("This piece matches preferred style.")
        elif "confidence" in exp:
            lines.append("This piece could have positive effect to boost your confidence based on your mood.")

        return f"{item['name']} selected because: " + " ".join(lines)
