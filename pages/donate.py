
import streamlit as st

st.set_page_config(
    page_title="Donate | Aurene",
    page_icon="♻️",
    layout="wide"
)
from navigation import apply_theme, show_navigation

apply_theme()
show_navigation()

st.title("GIVE CLOTHES A SECOND LIFE")
st.subheader("Your old clothes can create something new.")

st.write(
    "Donate clothing you no longer use. Suitable garments "
    "can be reused, while recoverable fabrics can be "
    "transformed into new Aurene Originals."
)

st.divider()

st.header("Submit a donation")

name = st.text_input("Your name")
email = st.text_input("Email address")

clothing_type = st.selectbox(
    "What are you donating?",
    ["Tops", "Trousers / Jeans", "Dresses",
     "Jackets", "Traditional wear", "Other"]
)

quantity = st.number_input(
    "Number of garments",
    min_value=1,
    max_value=100,
    value=1
)

condition = st.selectbox(
    "Condition of clothing",
    ["Like new", "Gently used", "Needs upcycling"]
)

photo = st.file_uploader(
    "Upload a photo of your donation",
    type=["jpg", "jpeg", "png"]
)

if st.button("SUBMIT DONATION"):
    if name and email:
        st.success("Your donation request has been submitted!")
        st.info("Your donation will be reviewed before credits are awarded.")
    else:
        st.warning("Please enter your name and email.")

st.divider()

st.header("How it works")

st.write("01 — Submit your clothing details.")
st.write("02 — Aurene reviews your donation.")
st.write("03 — Approved clothing is reused or upcycled.")
st.write("04 — Receive Aurene credits after approval.")
