
import streamlit as st

st.set_page_config(
    page_title="My Impact | Aurene",
    page_icon="🌱",
    layout="wide"
)
from navigation import apply_theme, show_navigation

apply_theme()
show_navigation()

st.title("MY IMPACT")
st.subheader("Small choices. A bigger difference.")

st.write(
    "Track your contribution towards a more "
    "responsible and circular fashion industry."
)

st.divider()

st.header("Your sustainability overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Garments Donated", "0")

with col2:
    st.metric("Garments Reused", "0")

with col3:
    st.metric("Credits Earned", "0")

st.divider()

st.header("Your contribution")

st.write(
    "Every approved donation and thoughtful purchase "
    "can help reduce clothing waste and encourage "
    "the reuse of valuable materials."
)

st.info(
    "Your personal impact statistics will appear here "
    "once your account activity is connected."
)

st.divider()

st.header("Your Aurene journey")

st.write("Start donating, discover sustainable fashion "
         "and track your progress here.")
