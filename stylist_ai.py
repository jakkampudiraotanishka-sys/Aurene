"""Aurene AI Stylist — talks to Google Gemini with text + clothing photos."""

import io
import os

import streamlit as st
from PIL import Image, ImageOps

from catalog import PRODUCTS

# "gemini-flash-latest" always points at Google's newest Flash model,
# so the app keeps working when older model names are retired.
# Override by adding GEMINI_MODEL = "..." to your secrets.
DEFAULT_MODEL = "gemini-flash-latest"

MAX_IMAGE_SIDE = 1024     # resize photos before sending (faster + cheaper)
HISTORY_LIMIT = 12        # how many past chat messages the AI sees


def _catalogue_text():
    lines = [
        f"- {p['name']} (₹{p['price']:,}, {p['category']}, {p['material']})"
        for p in PRODUCTS
    ]
    return "\n".join(lines)


SYSTEM_PROMPT = f"""
You are Aurene AI, the warm, stylish personal stylist for Aurene — a
sustainable fashion brand whose motto is "Wear more. Waste less."

What you do:
- When the user shares photos of clothes, first identify each piece briefly
  (type, colour, fabric/texture if visible, fit, vibe).
- Then build complete outfits from what they ALREADY own. Give each outfit a
  short name, list the pieces, and explain why it works (colour, proportion,
  occasion). Suggest shoes, layering and accessories.
- Offer quick styling tricks: tucks, cuffs, layering, re-wearing a piece
  three different ways.
- Only when a gap would genuinely help, suggest at most 1–2 Aurene pieces
  from the catalogue below, by exact name and price. Never push shopping.
- If something is worn out or no longer fits their style, gently mention
  they can donate it on the Aurene DONATE page to earn credits.
- If a photo is blurry, dark or not clothing, say so kindly and ask for a
  clearer shot (good light, item laid flat or on a hanger).

Style: friendly, confident, concise. Use short headings and bullet points.
Use ₹ for prices. Don't comment on the person's body — focus on the clothes.

Aurene catalogue:
{_catalogue_text()}
""".strip()


def prepare_image(raw_bytes):
    """Fix phone rotation, shrink, and convert to JPEG bytes."""
    img = Image.open(io.BytesIO(raw_bytes))
    img = ImageOps.exif_transpose(img)
    img = img.convert("RGB")
    img.thumbnail((MAX_IMAGE_SIDE, MAX_IMAGE_SIDE))
    out = io.BytesIO()
    img.save(out, format="JPEG", quality=85)
    return out.getvalue()


def get_api_key():
    try:
        return st.secrets["GEMINI_API_KEY"]
    except Exception:
        # Hosts like Render/Railway use environment variables instead
        return os.environ.get("GEMINI_API_KEY")


def ask_stylist(messages):
    """
    messages: list of {"role": "user"|"assistant", "content": str,
                       "images": [jpeg bytes, ...]}
    Returns the stylist's reply as markdown text.
    """
    from google import genai
    from google.genai import types

    api_key = get_api_key()
    if not api_key:
        return (
            "⚠️ **The AI stylist isn't connected yet.** Add your "
            "`GEMINI_API_KEY` to the app's secrets (see DEPLOY.md) and "
            "refresh the page."
        )

    try:
        model = st.secrets.get("GEMINI_MODEL", DEFAULT_MODEL)
    except Exception:
        model = DEFAULT_MODEL

    contents = []
    for msg in messages[-HISTORY_LIMIT:]:
        parts = [
            types.Part.from_bytes(data=img, mime_type="image/jpeg")
            for img in msg.get("images", [])
        ]
        if msg.get("content"):
            parts.append(types.Part.from_text(text=msg["content"]))
        if not parts:
            continue
        contents.append(
            types.Content(
                role="user" if msg["role"] == "user" else "model",
                parts=parts,
            )
        )

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.8,
            ),
        )
        return response.text or "I couldn't put together a look this time — please try again."
    except Exception as e:
        return (
            "I couldn't reach the styling studio just now. Please try again "
            f"in a moment.\n\n_Details: {type(e).__name__}: "
            f"{str(e)[:200]}_"
        )
