
import streamlit as st

st.set_page_config(
    page_title="AI Stylist | Aurene",
    page_icon="✨",
    layout="wide"
)
from navigation import apply_theme, show_navigation
from stylist_ai import ask_stylist, prepare_image

apply_theme()
show_navigation()

# ---------------- STATE ----------------

if "wardrobe" not in st.session_state:
    st.session_state.wardrobe = []          # list of jpeg bytes

if "camera_key" not in st.session_state:
    st.session_state.camera_key = 0

if "upload_key" not in st.session_state:
    st.session_state.upload_key = 0

if "stylist_messages" not in st.session_state:
    st.session_state.stylist_messages = [
        {
            "role": "assistant",
            "content": (
                "Hi, I'm **Aurene AI** ✦ your personal stylist.\n\n"
                "Snap or upload photos of clothes you own and I'll turn them "
                "into fresh outfits. You can also attach a photo right here "
                "in the chat, or just ask me anything about style, fabrics "
                "or caring for your clothes."
            ),
            "images": [],
        }
    ]

st.markdown("""
<style>
.stylist-hero {
    background: #E9DFD0;
    padding: 30px;
    text-align: center;
    margin-bottom: 18px;
}
.stylist-hero h1 {
    font-family: 'Playfair Display', serif;
    color: #49372C;
    letter-spacing: 3px;
    margin: 6px 0;
}
.stylist-label {
    color: #8B796B;
    font-size: 11px;
    letter-spacing: 3px;
}
[data-testid="stChatMessage"] {
    background-color: #EFE7DB;
    border-radius: 14px;
    padding: 14px;
}
[data-testid="stCameraInput"] {
    background-color: #E9DFD0;
    border-radius: 5px;
    padding: 10px;
}
</style>
<div class="stylist-hero">
    <div class="stylist-label">RESTYLE · YOUR AI STYLIST</div>
    <h1>YOUR WARDROBE, REIMAGINED</h1>
    <div style="color:#6D5B4F;">
        Photograph the clothes you already own. Aurene AI styles them for you.
    </div>
</div>
""", unsafe_allow_html=True)


def add_to_wardrobe(raw_bytes):
    try:
        st.session_state.wardrobe.append(prepare_image(raw_bytes))
        return True
    except Exception:
        st.warning("That file doesn't look like an image we can read.")
        return False


left, right = st.columns([1, 1.4], gap="large")

# ---------------- LEFT: BUILD THE WARDROBE ----------------

with left:
    st.markdown("### 1 · Add your clothes")

    cam_tab, upload_tab = st.tabs(["📷  TAKE A PHOTO", "⬆  UPLOAD PHOTOS"])

    with cam_tab:
        camera_on = st.toggle(
            "Open camera",
            help="Your browser will ask for camera permission."
        )
        if camera_on:
            shot = st.camera_input(
                "Lay the item flat or hang it up, in good light",
                key=f"camera_{st.session_state.camera_key}",
            )
            if shot is not None:
                if st.button("ADD PHOTO TO MY WARDROBE", width="stretch"):
                    if add_to_wardrobe(shot.getvalue()):
                        st.session_state.camera_key += 1
                        st.toast("Added to your wardrobe ✦")
                        st.rerun()
        st.caption(
            "On a phone, the **Upload** tab also lets you use your "
            "back camera."
        )

    with upload_tab:
        files = st.file_uploader(
            "Upload photos of your clothing",
            type=["jpg", "jpeg", "png", "webp"],
            accept_multiple_files=True,
            key=f"upload_{st.session_state.upload_key}",
        )
        if files:
            if st.button(
                f"ADD {len(files)} PHOTO(S) TO MY WARDROBE",
                width="stretch",
            ):
                added = sum(add_to_wardrobe(f.getvalue()) for f in files)
                st.session_state.upload_key += 1
                st.toast(f"{added} item(s) added ✦")
                st.rerun()

    # ---- wardrobe grid ----
    wardrobe = st.session_state.wardrobe
    st.markdown(f"### Your wardrobe ({len(wardrobe)})")

    if not wardrobe:
        st.info("Your digital wardrobe is empty. Add a photo to begin.")
    else:
        for start in range(0, len(wardrobe), 3):
            cols = st.columns(3)
            for offset, col in enumerate(cols):
                i = start + offset
                if i >= len(wardrobe):
                    break
                with col:
                    st.image(wardrobe[i], width="stretch")
                    if st.button("Remove", key=f"rm_{i}_{len(wardrobe)}",
                                 width="stretch"):
                        wardrobe.pop(i)
                        st.rerun()
        if st.button("Clear wardrobe"):
            st.session_state.wardrobe = []
            st.rerun()

    st.divider()
    st.markdown("### 2 · What are you dressing for?")

    occasion = st.selectbox(
        "Occasion",
        ["Casual day out", "College / School", "Work / Office", "Party",
         "Date night", "Formal event", "Wedding / Festive",
         "Vacation", "Other"]
    )

    style = st.selectbox(
        "Preferred style",
        ["Surprise me", "Minimalist", "Streetwear", "Casual",
         "Elegant", "Bohemian", "Indo-western"]
    )

    weather = st.select_slider(
        "Weather",
        ["Cold", "Cool", "Mild", "Warm", "Hot"],
        value="Warm",
    )

    extra = st.text_input(
        "Anything else? (optional)",
        placeholder="e.g. I want to wear my white sneakers",
    )

    create = st.button(
        "✦ CREATE MY OUTFITS",
        width="stretch",
        disabled=not wardrobe,
    )
    if not wardrobe:
        st.caption("Add at least one photo to create outfits.")

# ---------------- RIGHT: CHAT WITH THE STYLIST ----------------

with right:
    st.markdown("### 3 · Chat with Aurene AI")

    chat_box = st.container(height=640)

    with chat_box:
        for msg in st.session_state.stylist_messages:
            avatar = "✨" if msg["role"] == "assistant" else None
            with st.chat_message(msg["role"], avatar=avatar):
                if msg.get("images"):
                    st.image(msg["images"], width=110)
                if msg.get("content"):
                    st.markdown(msg["content"])

    if st.button("Start a new conversation"):
        del st.session_state.stylist_messages
        st.rerun()

# Chat input sits at the bottom of the page and accepts photos too.
prompt = st.chat_input(
    "Ask Aurene AI, or attach a photo of your clothes…",
    accept_file="multiple",
    file_type=["jpg", "jpeg", "png", "webp"],
)

new_message = None

if create and st.session_state.wardrobe:
    request = (
        f"Here {'is 1 piece' if len(wardrobe) == 1 else f'are {len(wardrobe)} pieces'} "
        f"from my wardrobe. Please style them for: {occasion}. "
        f"Preferred style: {style}. Weather: {weather}."
    )
    if extra:
        request += f" Note: {extra}"
    request += " Give me 2–3 complete outfit ideas."
    new_message = {
        "role": "user",
        "content": request,
        "images": list(st.session_state.wardrobe),
    }

elif prompt:
    images = []
    for f in (prompt.files or []):
        try:
            images.append(prepare_image(f.getvalue()))
        except Exception:
            pass
    text = (prompt.text or "").strip()
    if images and not text:
        text = "How can I style this?"
    if text or images:
        new_message = {"role": "user", "content": text, "images": images}

if new_message:
    st.session_state.stylist_messages.append(new_message)

    with chat_box:
        with st.chat_message("user"):
            if new_message["images"]:
                st.image(new_message["images"], width=110)
            st.markdown(new_message["content"])

        with st.chat_message("assistant", avatar="✨"):
            with st.spinner("Styling your look…"):
                reply = ask_stylist(st.session_state.stylist_messages)
            st.markdown(reply)

    st.session_state.stylist_messages.append(
        {"role": "assistant", "content": reply, "images": []}
    )
