import streamlit as st


from pages.pages_1 import page2
from pages.pages_2 import page3


def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")


page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()