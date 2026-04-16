import streamlit as st
import pandas as pd

# --- Styling ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500&family=Inter:wght@300;400&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #ffe4ec, #ffd6e7, #ffc2dd);
}

h1 {
    font-family: 'Playfair Display', serif;
    color: #b03060;
    text-align: center;
}

.section {
    background-color: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("Outfit Planning Assistant")

st.markdown("<div class='section'>Plan an outfit based on context, style direction, and conditions.</div>", unsafe_allow_html=True)

# --- Layout ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    occasion = st.selectbox("Occasion", ["School", "Gym", "Social Event", "Date", "Casual"])
    style = st.selectbox("Style", ["Minimal", "Sport", "Elevated"])
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    weather = st.selectbox("Weather", ["Warm", "Cold", "Rain"])
    formality = st.slider("Formality", 1, 10, 5)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Button ---
generate = st.button("Generate Outfit")

# --- Logic + Output ---
if generate:

    outfit = ""
    notes = []
    pieces = []

    if occasion == "School":
        outfit = "Layered everyday outfit"
        pieces = ["Jeans", "Top", "Sneakers"]
    elif occasion == "Gym":
        outfit = "Performance outfit"
        pieces = ["Leggings", "Sports top", "Running shoes"]
    elif occasion == "Social Event":
        outfit = "Statement outfit"
        pieces = ["Top", "Bottom", "Accessories"]
    elif occasion == "Date":
        outfit = "Balanced outfit"
        pieces = ["Nice top", "Jeans or skirt", "Shoes"]
    else:
        outfit = "Relaxed outfit"
        pieces = ["Sweatpants", "Hoodie", "Sneakers"]

    if style == "Sport":
        notes.append("Incorporate athletic elements")
    elif style == "Elevated":
        notes.append("Use structured pieces and accessories")

    if formality > 7:
        notes.append("Lean toward more polished items")
    elif formality < 4:
        notes.append("Focus on comfort")

    if weather == "Cold":
        notes.append("Add layers or jacket")
    elif weather == "Rain":
        notes.append("Use water-resistant items")

    # --- Output Layout ---
    st.markdown("<div class='section'>", unsafe_allow_html=True)

    st.subheader("Outfit Summary")
    st.write(outfit)

    st.subheader("Suggested Pieces")
    for p in pieces:
        st.write("- " + p)

    st.subheader("Styling Notes")
    for n in notes:
        st.write("- " + n)

    st.markdown("</div>", unsafe_allow_html=True)

    # --- Image ---
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader("Visual Direction")

    image_map = {
        "Minimal": "https://images.unsplash.com/photo-1490481651871-ab68de25d43d",
        "Sport": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438",
        "Elevated": "https://images.unsplash.com/photo-1520974735194-1e2b8b8c0b4f"
    }

    st.image(image_map[style], use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- Chart ---
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader("Style Profile")

    data = pd.DataFrame({
        "Category": ["Comfort", "Style", "Function"],
        "Score": [
            10 - formality if formality < 5 else 5,
            formality,
            7 if weather == "Rain" else 5
        ]
    })

    st.bar_chart(data.set_index("Category"))
    st.markdown("</div>", unsafe_allow_html=True)

