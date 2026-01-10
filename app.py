import streamlit as st
from google import genai
from logic.filters import hard_filter
from logic.scoring import select_best_items
from logic.explain import explain_item
from services.weather_service import get_weather_by_city
from services.llm_service import generate_llm_explanation



from data.loader import load_items

client = genai.Client()

st.set_page_config(
    page_title="AI Outfit Recommendation",
    page_icon="👗",
    layout="wide"
)

st.title("👗 AI Outfit Recommendation Assistant")

# ---- LAYOUT ----
left, center, right = st.columns([1, 1.2, 1])

# ---- LEFT: USER INPUT ----
with left:
    st.subheader("🧩 Kullanıcı Bilgileri")

    city = st.text_input("📍 Şehir", placeholder="Örn: Bursa")

    mood = st.selectbox(
        "🧠 Ruh hali",
        ["happy", "relaxed", "sad", "depressed", "anxious"]
    )

    occasion = st.selectbox(
        "📅 Amaç",
        ["work", "meeting", "hangout", "date", "travel"]
    )

    style = st.selectbox(
        "👕 Stil",
        ["casual", "smart-casual", "business-casual", "elegant"]
    )

    generate = st.button("✨ Kombin Öner")

# ---- PROCESS ----
if generate and city:
    weather = get_weather_by_city(city)

    user_input = {
        "weather": weather,
        "occasion": occasion,
        "style": style,
        "season": "all",
        "mood": mood
    }

    items = load_items()
    filtered_items = hard_filter(items, user_input)
    final_outfit = select_best_items(filtered_items, user_input)

    # ---- CENTER: OUTFIT ----
    with center:
        st.subheader("👚 Seçilen Kombin")
        st.caption(f"🌤️ {city} – {weather}")

        for category, scored_item in final_outfit.items():
            item = scored_item["item"]
            st.markdown(f"### {category.upper()}")
            st.write(item["name"])

    # ---- RIGHT: EXPLANATION ----
    with right:
        st.subheader("🧠 AI Açıklaması")

        llm_text = generate_llm_explanation(
            outfit=final_outfit,
            user_input=user_input,
            client=client
        )

        st.markdown("### 🤖 LLM Yorumu")
        st.write(llm_text)

elif generate and not city:
    st.warning("Lütfen şehir gir.")
