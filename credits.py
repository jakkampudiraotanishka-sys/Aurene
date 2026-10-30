
import streamlit as st

st.set_page_config(
    page_title="Credits | Aurene",
    page_icon="✦",
    layout="wide"
)
from navigation import apply_theme, show_navigation

apply_theme()
show_navigation()

st.title("AURENE CREDITS")
st.subheader("Good choices deserve rewards.")

st.write(
    "Earn credits by donating pre-loved clothing "
    "and redeem them on eligible Aurene purchases."
)

st.divider()

st.header("Your rewards")

col1, col2 = st.columns(2)

with col1:
    st.metric("Available Credits", "0")

with col2:
    st.metric("Total Credits Earned", "0")

st.divider()

st.header("How to earn credits")

st.write("01 — Submit a clothing donation.")
st.write("02 — Wait for your donation to be reviewed.")
st.write("03 — Receive credits when your donation is approved.")

st.divider()

st.header("Your transactions")

st.info("Your credit history will appear here.")

st.divider()

st.header("Redeem your credits")

st.write(
    "Use your earned credits towards eligible "
    "Aurene Originals purchases."
)

if st.button("EXPLORE THE SHOP"):
    st.switch_page("pages/shop.py")
