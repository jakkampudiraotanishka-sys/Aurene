
import streamlit as st

st.set_page_config(
    page_title="Aurene | Sustainable Fashion",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)
from navigation import apply_theme, show_navigation

apply_theme()
show_navigation()

# COLOUR PALETTE
CREAM = "#F8F4EC"
BEIGE = "#E9DFD0"
BROWN = "#49372C"
DARK = "#30231D"
MUTED = "#8B796B"

# CUSTOM WEBSITE STYLING
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600&family=DM+Sans:wght@400;500;600&display=swap');

    .stApp {{
        background-color: {CREAM};
        color: {DARK};
    }}

    h1, h2, h3 {{
        font-family: 'Playfair Display', serif !important;
        color: {BROWN} !important;
    }}

    p, div, label {{
        font-family: 'DM Sans', sans-serif;
    }}

    .block-container {{
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }}

    .brand {{
        font-family: 'Playfair Display', serif;
        font-size: 43px;
        letter-spacing: 7px;
        color: {BROWN};
        text-align: center;
        padding: 10px;
    }}

    .tagline {{
        text-align: center;
        color: {MUTED};
        letter-spacing: 4px;
        font-size: 10px;
        margin-bottom: 25px;
    }}

    .hero {{
        background-color: {BEIGE};
        padding: 65px 45px;
        text-align: center;
        border-radius: 3px;
    }}

    .hero-label {{
        letter-spacing: 4px;
        font-size: 11px;
        color: {MUTED};
    }}

    .hero-title {{
        font-family: 'Playfair Display', serif;
        font-size: 54px;
        color: {BROWN};
        margin: 20px 0;
        line-height: 1.2;
    }}

    .hero-text {{
        color: {DARK};
        font-size: 15px;
        line-height: 1.8;
        max-width: 600px;
        margin: auto;
    }}

    .section-label {{
        letter-spacing: 3px;
        font-size: 10px;
        color: {MUTED};
    }}

    .info-card {{
        background: #EFE8DD;
        padding: 25px;
        min-height: 175px;
        border-radius: 3px;
        margin-bottom: 10px;
    }}

    .info-card h3 {{
        font-size: 23px;
    }}

    .info-card p {{
        font-size: 13px;
        color: {MUTED};
        line-height: 1.7;
    }}

    div.stButton > button {{
        background-color: {BROWN};
        color: {CREAM};
        border: 1px solid {BROWN};
        border-radius: 2px;
        padding: 10px 25px;
        font-size: 13px;
    }}

    div.stButton > button:hover {{
        background-color: {DARK};
        color: white;
        border-color: {DARK};
    }}

    hr {{
        border-color: {BEIGE};
    }}
</style>
""", unsafe_allow_html=True)


# HERO SECTION
st.markdown("""
<div class="hero">
    <div class="hero-label">A NEW PERSPECTIVE ON FASHION</div>
    <div class="hero-title">
        Fashion that comes<br>full circle.
    </div>
    <div class="hero-text">
        Discover your personal style, rediscover your wardrobe
        and make more thoughtful fashion choices.
        Because looking good and doing good should go hand in hand.
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# AI STYLIST SECTION
st.markdown('<div class="section-label">01 — PERSONAL STYLE</div>',
            unsafe_allow_html=True)

st.header("A wardrobe full of possibilities.")

st.write(
    "Your existing clothes, reimagined. Snap a photo and let our AI stylist "
    "discover new combinations and help you create outfits "
    "for every occasion."
)

if st.button("DISCOVER YOUR STYLE"):
    st.switch_page("pages/restyle.py")

st.divider()

# SUSTAINABLE COLLECTION
st.markdown('<div class="section-label">02 — AURENE ORIGINALS</div>',
            unsafe_allow_html=True)

st.header("Thoughtfully made. Beautifully worn.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>Reimagined Collection</h3>
        <p>
        New designs created using recovered fabrics,
        donated garments and upcycled textiles.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>Organic Collection</h3>
        <p>
        Everyday essentials made using organic cotton,
        bamboo-based fabrics and responsibly sourced materials.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# REWEAR SECTION
st.markdown('<div class="section-label">03 — GIVE CLOTHES A SECOND LIFE</div>',
            unsafe_allow_html=True)

st.header("Your old clothes deserve a new story.")

st.write(
    "Donate your pre-loved clothing, contribute to a circular "
    "fashion system and receive Aurene credits when your "
    "donation is approved."
)

if st.button("EXPLORE REWEAR"):
    st.switch_page("pages/donate.py")

st.divider()

# FOOTER
st.markdown(
    '<div style="text-align:center; padding:25px; color:#8B796B;">'
    '<div style="font-family:Playfair Display; font-size:25px; '
    'letter-spacing:5px;">AURENE</div>'
    '<p>WEAR MORE. WASTE LESS. DISCOVER MORE.</p>'
    '<small>Fashion with a purpose. © 2026 Aurene.</small>'
    '</div>',
    unsafe_allow_html=True
)