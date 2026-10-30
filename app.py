
import streamlit as st

st.set_page_config(
    page_title="Aurene | Sustainable Fashion",
    page_icon="🌿",
    layout="wide"
)

pages = [
    st.Page("home.py", title="HOME", default=True),
    st.Page("pages/shop.py", title="SHOP"),
    st.Page("pages/restyle.py", title="AI STYLIST"),
    st.Page("pages/community.py", title="COMMUNITY"),
    st.Page("pages/donate.py", title="DONATE"),
    st.Page("pages/credits.py", title="CREDITS"),
    st.Page("pages/impact.py", title="MY IMPACT")
]

page = st.navigation(pages, position="hidden")
page.run()
