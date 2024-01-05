import streamlit as st
import os
from src.reading_readme import ReadingReadMe

def main_page(path = None):
    st.title("Welcome to my website!")
    st.write("This is a website where I will be posting my research papers and insights out of it.")

def page_name(path):
    # drop down menu
    file_names = os.path.join(path, '*.md')
    file_names = os.listdir(path)
    selected_file = st.sidebar.selectbox("Select a file", file_names)
    selected_file = os.path.join(path, selected_file)
    file_info = ReadingReadMe(selected_file)
    file_info.run()
    file_info.get_markdown()

page_names_to_funcs = {
    "Main Page": main_page,
    "Diffusion": page_name,
    "DeepFakeResearch": page_name,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page](f'research_papers/{selected_page}')