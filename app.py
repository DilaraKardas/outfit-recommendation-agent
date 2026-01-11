import json
import streamlit as st
from google import genai
from logic.filters import hard_filter
from logic.scoring import select_best_items
from logic.explain import explain_item
from services.weather_service import get_weather_by_city
from services.weather_service import get_weather_by_coordinates
from services.llm_service import generate_llm_explanation
from data.loader import load_items
from services.nlp_parser import parse_user_input_with_llm
import streamlit.components.v1 as components
from collections import defaultdict

client = genai.Client()

st.set_page_config(
    page_title="AI Outfit Recommendation",
    page_icon="👗",
    layout="wide"
)
st.title("👗 AI Outfit Recommendation Assistant")

# ---- LOCATION & WEATHER (BACKGROUND) ----
if "coords" not in st.session_state:
    location_data = components.html(
        """
        <script>
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const coords = {
                    lat: position.coords.latitude,
                    lon: position.coords.longitude
                };
                document.body.innerText = JSON.stringify(coords);
            },
            (error) => {
                document.body.innerText = JSON.stringify({error: error.message});
            }
        );
        </script>
        """,
        height=0,
    )

    if location_data:
        try:
            st.session_state.coords = json.loads(location_data)
        except:
            st.session_state.coords = None

if "weather" not in st.session_state:
    if st.session_state.get("coords") and "lat" in st.session_state.coords:
        st.session_state.weather = get_weather_by_coordinates(
            st.session_state.coords["lat"],
            st.session_state.coords["lon"]
        )
    else:
        st.session_state.weather = "cold"


# ---- LAYOUT ----
left, center, right = st.columns([1, 1.2, 1])

# ---- LEFT: USER INPUT ----
with left:
    user_text = st.text_area(
        "Bugünkü planın nedir ve nasıl hissediyorsun?",
        placeholder="Bugün enerjik hissediyorum, işe gideceğim ama çok resmi olmak istemiyorum."
    )

    if st.button("Kombin öner"):
        if not user_text.strip():
            st.warning("Biraz ipucu vermelisin 🙂")
            st.stop()
        
        with st.spinner("Düşünüyorum..."):
            parsed = parse_user_input_with_llm(client, user_text)

        user_input = {
            "mood": parsed["mood"],
            "occasion": parsed["occasion"],
            "style": parsed["style"],
            "weather": st.session_state.weather,
            #"season": parsed.get("season", "all")
        }
        
        items = load_items()
        st.write("DEBUG - Toplam yüklenen kıyafet:", len(items))  # Kaç kıyafet var?
        st.write("DEBUG - user_input:", user_input)  # Hangi filtreler uygulanıyor?

        filtered_items = hard_filter(items, user_input)
        st.write("DEBUG - Filtreden geçen:", len(filtered_items))  # Kaç tanesi geçti?
        filtered_items = hard_filter(items, user_input)
        final_outfit = select_best_items(filtered_items, user_input)
        
        # Buton içinde, kaydetmeden önce:
        st.write("DEBUG - filtered_items:", len(filtered_items))
        st.write("DEBUG - final_outfit:", final_outfit)

        # Session state'e kaydediliyor
        st.session_state.parsed = parsed
        st.session_state.filtered_items = filtered_items
        st.session_state.final_outfit = final_outfit
        st.session_state.user_input = user_input

# Eğer session state'te sonuçlar varsa göster
if "final_outfit" in st.session_state:
    parsed = st.session_state.parsed
    filtered_items = st.session_state.filtered_items
    final_outfit = st.session_state.final_outfit
    user_input = st.session_state.user_input

    with left:
        st.subheader("🧠 Ayrıştırılan Bilgiler: ")
        st.json(parsed)

    # Gruplama
    grouped_filtered = defaultdict(list)
    for item in filtered_items:
        grouped_filtered[item["category"]].append(item)

    # ---- CENTER: OUTFIT ----
    with center:
        st.subheader("🧪 Filtrelerden Geçen Kıyafetler")
        st.caption("Kurallara uyan adaylar")

        for category, items in grouped_filtered.items():
            item_names = [item["name"] for item in items]
            items_string = ", ".join(item_names)
            st.markdown(f"**{category.upper()}:** {items_string}")

        st.divider()

        st.subheader("👚 Final Kombin")
        st.caption("Skorlama sonrası seçilenler")

        if final_outfit:  # Boş değilse
            cols = st.columns(len(final_outfit))

            for idx, (layer, scored_item) in enumerate(final_outfit.items()):
                item = scored_item["item"]
                with cols[idx % len(cols)]:
                    st.info(f"**{layer.upper()}**")
                    st.write(f"✨ {item['name']}")
                    st.caption(f"Skor: {scored_item['score']}")
        else:
            st.warning("Uygun kombin bulunamadı.")

    # ---- RIGHT: EXPLANATION ----
    with right:
        st.subheader("🧠 AI Açıklaması")

        # llm_text = generate_llm_explanation(
        #     outfit=final_outfit,
        #     user_input=user_input,
        #     client=client
        # )

        st.markdown("### 🤖 LLM Yorumu")
        # st.write(llm_text)