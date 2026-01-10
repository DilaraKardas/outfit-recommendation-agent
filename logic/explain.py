from services.llm_service import generate_explanation_with_llm

#llm çalışmazsa kural tabanlı açıklama döner
def build_rule_explanation(scored_item):
    return " ".join(scored_item["explanation"])

def explain_item(scored_item, user_input, client = None, use_llm=True):
    rule_text = " ".join(scored_item["explanation"])

    if not use_llm or client is None:
        return rule_text
    
    return generate_explanation_with_llm(
        client = client,
        item_name = scored_item["item"]["name"],
        rule_explanation = rule_text,
        user_input = user_input
    )
