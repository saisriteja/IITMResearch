import streamlit as st
import os
from src.reading_readme import ReadingReadMe


def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")



def diffusion(path = 'research_papers/diffusion'):

    # drop down menu
    file_names = os.path.join(path, '*.md')
    file_names = os.listdir(path)

    selected_file = st.sidebar.selectbox("Select a file", file_names)

    selected_file = os.path.join(path, selected_file)

    file_info = ReadingReadMe(selected_file)

    file_info.run()

    # # show the dict in the streamlit
    # for key, value in file_info.information.items():
    #     st.markdown(f"## {key}")
    #     for point in value:
    #         st.markdown(f"- {point}")

    file_info.get_markdown()




page_names_to_funcs = {
    "Main Page": main_page,
    "Diffusion": diffusion,
}
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()