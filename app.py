import streamlit as st
<<<<<<< HEAD
st.markdown(
    """
    <style>
    body {
        background-color: #ffe6f0;
    }
    .stApp {
        background-color: #ffe6f0;
    }
    h1 {
        color: #ff4da6;
        text-align: center;
    }
    p {
        color: #cc0066;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("Outfit Planner App")

# Description
st.write("This app helps you plan outfits based on your style and occasion.")

# User Inputs
occasion = st.selectbox(
    "Where are you going?",
    ["School", "Gym", "Party", "Date", "Casual Day"]
)

style = st.radio(
    "Choose your style:",
    ["Casual", "Sporty", "Dressy"]
)

# Output (changes based on input)
st.subheader("Outfit Suggestion")
if occasion == "School":
    if style == "Casual":
        st.write("Wear jeans, a hoodie, and sneakers.")
    elif style == "Sporty":
        st.write("Wear leggings, a sweatshirt, and running shoes.")
    else:
        st.write("Wear a cute top, jeans, and boots.")

elif occasion == "Gym":
    st.write("Wear athletic shorts or leggings with a workout top and sneakers.")

elif occasion == "Party":
    if style == "Dressy":
        st.write("Wear a dress with heels.")
    else:
        st.write("Wear a stylish top with jeans and accessories.")

elif occasion == "Date":
    st.write("Wear something cute and comfortable, like a nice top with jeans or a dress.")

elif occasion == "Casual Day":
    st.write("Wear comfy clothes like leggings, a sweatshirt, and sneakers.")
