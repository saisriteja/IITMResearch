import streamlit as st
import os
from src.reading_readme import ReadingReadMe

def main_page(path = None):
    st.title("Welcome to my website!")
    st.write("This is a website where I will be posting my research papers and insights out of it.")

from src.research_info import get_all_info

def page_name():
    # drop down menu
    papers = os.listdir('research_papers/all/')

    selected_paper = st.sidebar.selectbox("Select a paper", papers)
    file_info = get_all_info(f'research_papers/all/{selected_paper}')

    # make it as markdown content
    for key, value in file_info.items():
        st.write(f"## {key}")
        for point in value:
            st.write(f"- {point}")

page_names_to_funcs = {
    "Main Page": main_page,
    "Research Papers": page_name
}


selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()