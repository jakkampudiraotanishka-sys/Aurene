
import streamlit as st

st.set_page_config(
    page_title="Community | Aurene",
    page_icon="♡",
    layout="wide"
)
from navigation import apply_theme, show_navigation

apply_theme()
show_navigation()

st.title("THE AURENE COMMUNITY")
st.subheader("Inspiration looks better when shared.")

st.write(
    "Discover new styles, share your outfits and "
    "find inspiration from the Aurene community."
)

st.divider()

st.header("Share your style")

caption = st.text_input(
    "Give your outfit a title or caption",
    placeholder="e.g. My everyday summer look"
)

photo = st.file_uploader(
    "Upload your outfit",
    type=["jpg", "jpeg", "png"]
)

if st.button("SHARE POST"):
    if photo and caption:
        st.success("Your post is ready to be added!")
    else:
        st.warning("Please add a photo and caption.")

st.divider()

st.header("Explore")

st.write(
    "Discover outfits and creative combinations "
    "shared by other Aurene members."
)

st.info("Community posts and interactions will appear here.")
