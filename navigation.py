
import streamlit as st

# AURENE COLOUR PALETTE
CREAM = "#F8F4EC"
BEIGE = "#E9DFD0"
BROWN = "#49372C"
DARK = "#30231D"
MUTED = "#8B796B"


def apply_theme():

    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600&family=DM+Sans:wght@400;500;600&display=swap');

        .stApp {{
            background-color: {CREAM};
            color: {DARK};
        }}

        html, body, [class*="css"] {{
            font-family: 'DM Sans', sans-serif;
        }}

        h1, h2, h3 {{
            font-family: 'Playfair Display', serif !important;
            color: {BROWN} !important;
        }}

        .block-container {{
            max-width: 1250px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }}

        [data-testid="stSidebar"] {{
            background-color: {BEIGE};
        }}

        div.stButton > button {{
            background-color: {BROWN};
            color: {CREAM};
            border: 1px solid {BROWN};
            border-radius: 3px;
            padding: 10px 18px;
        }}

        div.stButton > button:hover {{
            background-color: {DARK};
            color: white;
        }}

        div[data-testid="stMetric"] {{
            background-color: {BEIGE};
            padding: 20px;
            border-radius: 5px;
        }}

        div[data-testid="stFileUploader"] {{
            background-color: {BEIGE};
            border-radius: 5px;
            padding: 10px;
        }}

        hr {{
            border-color: {BEIGE};
        }}

        a {{
            color: {BROWN} !important;
        }}
    </style>
    """, unsafe_allow_html=True)


def show_navigation():

    st.markdown(
        f"""
        <div style="text-align:center; padding:10px 0 2px;">
            <div style="
                font-family:'Playfair Display',serif;
                font-size:38px;
                letter-spacing:9px;
                color:{BROWN};
            ">AURENE</div>
            <div style="
                font-size:9px;
                letter-spacing:4px;
                color:{MUTED};
            ">CONSCIOUSLY CREATED. THOUGHTFULLY WORN.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # MAIN NAVIGATION
    columns = st.columns(6)

    links = [
        ("HOME", "home.py"),
        ("SHOP", "pages/shop.py"),
        ("✦ AI STYLIST", "pages/restyle.py"),
        ("DISCOVER", "pages/community.py"),
        ("DONATE", "pages/donate.py"),
        ("MY IMPACT", "pages/impact.py")
    ]

    for column, (label, path) in zip(columns, links):
        with column:
            st.page_link(
                path,
                label=label,
                width="stretch"
            )

    st.divider()

    # SECONDARY NAVIGATION
    left, right = st.columns([5, 1])

    with left:
        st.caption("✦ YOUR STYLE. YOUR COMMUNITY. A BETTER FUTURE.")

    with right:
        st.page_link(
            "pages/credits.py",
            label="✧ CREDITS",
            width="stretch"
        )

    st.divider()
