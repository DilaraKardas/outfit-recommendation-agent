import json

def parse_user_input_with_llm(client, user_text):
    prompt = f"""

You are an information extraction system.

TASK:
Extract the following fields from the user text:
- mood
- occasion
- style

Allowed values:
mood:
happy, relaxed, sad, depressed, anxious, stressed

occasion:
work, meeting, hangout, date, travel, party

style:
casual, smart-casual, buisness-casual, elegant

RULES:
- Respond with ONLY valid JSON
- Do NOT add explanations
- Do NOT use markdown
- Do NOT add extra text
- Keys must be exactly: mood, occasion, style
- Values must be lowercase strings

User text:
\"\"\"{user_text}\"\"\"

JSON:
"""
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )
    try:
        text = response.text.strip()
        return json.loads(text)
    except Exception:
        return {
            "mood": "happy",
            "occasion": "hangout",
            "style" : "casual"
        }
"""
"""