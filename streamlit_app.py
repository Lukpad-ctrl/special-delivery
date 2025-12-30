import streamlit as st

st.set_page_config(page_title="Special Delivery", layout="centered")

st.markdown("""
<style>
button {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
body {
    background-color: #191970;
}
.stApp {
    background-color: #191970;
    color: white;
    font-family: monospace;
}
.header {
    font-size: 20px;
    text-align: center;
    margin-top: 40px;
}
.footer {
    position: fixed;
    bottom: 20px;
    width: 100%;
    text-align: center;
    font-size: 14px;
    opacity: 0.8;
}
</style>
""", unsafe_allow_html=True)


st.markdown("<div class='header'> special-delivery</div>", unsafe_allow_html=True)
st.markdown("### Do you love me?")

col1, col2 = st.columns(2)

with col1:
    if st.button("YES"):
        st.success("I know 💚 Happy New Year  \n"
    "Thanks for being my fav person  \n"
    "May this year be full of successful builds"
        )

with col2:
    if st.button("NO"):
        st.warning("Nice try 😌")

st.markdown(
    "<div class='footer'>Made with ❤️ for you</div>",
    unsafe_allow_html=True
)
