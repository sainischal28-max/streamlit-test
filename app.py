import streamlit as st

st.title("Product Help & Feedback App")

product = st.selectbox(
    "Select a product",
    ["Jodo Solar Filter", "Educational Toy", "Learning Kit"]
)

st.header(f"How to use: {product}")

if product == "Jodo Solar Filter":
    st.write("""
    1. Place the filter in sunlight.
    2. Connect it properly.
    3. Check if the indicator is working.
    4. Clean it regularly.
    """)

elif product == "Educational Toy":
    st.write("""
    1. Open the toy carefully.
    2. Read the age instructions.
    3. Use it with the activity guide.
    4. Store it safely after use.
    """)

else:
    st.write("""
    1. Open the learning kit.
    2. Follow the guide.
    3. Watch the demo video.
    4. Give feedback after use.
    """)

st.header("Feedback")

name = st.text_input("Name")
rating = st.slider("Rating", 1, 5)
feedback = st.text_area("Feedback")

if st.button("Submit"):
    st.success("Feedback submitted!")
