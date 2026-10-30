
import streamlit as st

st.set_page_config(
    page_title="Shop | Aurene",
    page_icon="🛍️",
    layout="wide"
)

from navigation import apply_theme, show_navigation

apply_theme()
show_navigation()

# ---------------- PRODUCT CATALOGUE ----------------

from catalog import PRODUCTS as products

# ---------------- SESSION STATE ----------------

if "cart" not in st.session_state:
    st.session_state.cart = []

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

# ---------------- SHOP DESIGN ----------------

st.markdown("""
<style>
.shop-heading {
    background: #E9DFD0;
    padding: 30px;
    text-align: center;
    margin-bottom: 22px;
}
.shop-heading h1 {
    font-family: 'Playfair Display', serif;
    color: #49372C;
    font-size: 36px;
    letter-spacing: 3px;
}
.shop-heading p {
    color: #6D5B4F;
}
.product-card {
    background: #FFFFFF;
    padding: 12px;
    border: 1px solid #E9DFD0;
    border-radius: 7px;
    margin-bottom: 10px;
}
.product-name {
    font-family: 'Playfair Display', serif;
    color: #49372C;
    font-size: 18px;
    font-weight: 600;
    min-height: 48px;
}
.product-price {
    color: #49372C;
    font-size: 19px;
    font-weight: 700;
}
.product-info {
    color: #8B796B;
    font-size: 13px;
}
.shop-label {
    color: #8B796B;
    font-size: 11px;
    letter-spacing: 2px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown("""
<div class="shop-heading">
    <div class="shop-label">AURENE ORIGINALS · CONSCIOUS COLLECTIONS</div>
    <h1>THE WAY WE WEAR THE FUTURE</h1>
    <p>Thoughtfully made. Beautifully worn.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- SEARCH ----------------

search_col, bag_col = st.columns([5, 1])

with search_col:
    search = st.text_input(
        "Search the collection",
        placeholder="Search shirts, denim, bags, organic cotton..."
    )

with bag_col:
    st.write("")
    st.markdown(
        f"**✧ BAG ({len(st.session_state.cart)})**"
    )

st.divider()

# ---------------- FILTERS + PRODUCTS ----------------

filter_col, products_col = st.columns([1, 3.5])

with filter_col:
    st.markdown("### FILTER BY")

    category = st.radio(
        "Category",
        ["All", "Women's", "Men's", "Accessories"]
    )

    material = st.radio(
        "Material",
        ["All materials", "Organic Cotton", "Upcycled Denim",
         "Reclaimed Fabric", "Recycled Fabric", "Upcycled Fabric"]
    )

    max_price = st.slider(
        "Maximum price",
        min_value=500,
        max_value=3000,
        value=3000,
        step=100
    )

    sorting = st.selectbox(
        "Sort products",
        ["Featured", "Price: Low to High", "Price: High to Low", "Top Rated"]
    )

with products_col:

    filtered = products.copy()

    if category != "All":
        filtered = [
            p for p in filtered
            if p["category"] == category
        ]

    if material != "All materials":
        filtered = [
            p for p in filtered
            if p["material"] == material
        ]

    filtered = [
        p for p in filtered
        if p["price"] <= max_price
    ]

    if search:
        filtered = [
            p for p in filtered
            if search.lower() in p["name"].lower()
            or search.lower() in p["material"].lower()
            or search.lower() in p["category"].lower()
        ]

    if sorting == "Price: Low to High":
        filtered.sort(key=lambda p: p["price"])
    elif sorting == "Price: High to Low":
        filtered.sort(key=lambda p: p["price"], reverse=True)
    elif sorting == "Top Rated":
        filtered.sort(key=lambda p: p["rating"], reverse=True)

    st.markdown("### Explore the collection")
    st.caption(f"{len(filtered)} products available")

    if not filtered:
        st.info("No products found. Try changing your filters.")

    for start in range(0, len(filtered), 3):
        cols = st.columns(3)

        for col, product in zip(cols, filtered[start:start + 3]):
            with col:

                st.image(
                    product["image"],
                    width="stretch"
                )

                st.markdown(
                    f'<div class="product-name">{product["name"]}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="product-info">{product["material"]} · {product["category"]}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="product-price">₹{product["price"]:,}</div>',
                    unsafe_allow_html=True
                )

                st.caption(f"★ {product['rating']} / 5.0")

                with st.expander("View product details"):
                    st.write(product["description"])
                    st.write(f"Material: {product['material']}")

                key = product["name"]

                if st.button(
                    "ADD TO BAG",
                    key=f"bag_{key}",
                    width="stretch"
                ):
                    st.session_state.cart.append(product)
                    st.toast("Added to your bag!")
                    st.rerun()

                if st.button(
                    "♡ ADD TO WISHLIST",
                    key=f"wish_{key}",
                    width="stretch"
                ):
                    if key not in st.session_state.wishlist:
                        st.session_state.wishlist.append(key)
                        st.toast("Added to wishlist!")
                    else:
                        st.toast("Already saved!")

                st.write("")

# ---------------- SHOPPING BAG ----------------

st.divider()
st.markdown("## YOUR SHOPPING BAG")

if st.session_state.cart:

    total = 0

    for i, item in enumerate(st.session_state.cart):
        c1, c2, c3 = st.columns([4, 1, 1])

        with c1:
            st.write(item["name"])

        with c2:
            st.write(f"₹{item['price']:,}")

        with c3:
            if st.button("Remove", key=f"remove_{i}"):
                st.session_state.cart.pop(i)
                st.rerun()

        total += item["price"]

    st.markdown(f"### Total: ₹{total:,}")

    st.button(
        "PROCEED TO CHECKOUT",
        disabled=True,
        width="stretch"
    )
    st.caption("Demo checkout. Payment integration will be added later.")

else:
    st.write("Your bag is waiting for something special.")

st.divider()

st.caption("AURENE · CONSCIOUSLY CREATED. THOUGHTFULLY WORN.")
