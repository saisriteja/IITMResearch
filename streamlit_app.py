from curses import keyname
import json
import streamlit as st
import os
from src.reading_readme import ReadingReadMe
import pandas as pd

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




def tag_finder():
    all_meta  = json.load(open('cache/research_papers.json'))
    all_tags = []
    for papername, tags in all_meta.items():
        all_tags.extend(tags)   

    unq_tags = list(set(all_tags))

    selected_tag = st.sidebar.selectbox("Select a paper", unq_tags)


    papers_names = []

    for papername, tags in all_meta.items():
        if selected_tag in tags:
            papers_names.append(papername)


    # make a dataframe of things    
            
    data = pd.DataFrame()

    for paper in papers_names:
        file_info = get_all_info(f'research_papers/all/{paper}')
        data = data._append(file_info, ignore_index=True)


    # import streamlit as st

    gaps_df_on = st.toggle('Gaps in research', key = 'gaps')
    if gaps_df_on:
        gaps_df = data[['Gaps in research ps', 'Gaps in methodology', 'Explicit Limits']]   
        st.table(gaps_df)

    change_df_on = st.toggle('changes that can be done', key = 'change')
    if change_df_on:
        change_df = data[['Research PaperName', 'Changing Task of Interest', 'Change in eval strategy', 'change the proposed method']]
        st.table(change_df)

    paper_structure_df_on = st.toggle('Paper structure', key = 'paper_structure')
    if paper_structure_df_on:
        paper_structure_df = data[['Research PaperName','Global Structure', 'Seq of figs', 'Abstract Structure', 'Intro Structure', 'Related work structure', 'Conclusion Structure', 'method and exp structure']]
        st.table(paper_structure_df)


    paper_info_df_on = st.toggle('Meta Information about the paper', key = 'paper_info')
    if paper_info_df_on:
        paper_info_df = data[['Research PaperName', 'Priority', 'Conference', 'Year', 'Lab', 'Github_Project', 'Abstract', 'Results', 'Future Works']]
        st.table(paper_info_df)


        
page_names_to_funcs = {
    "Main Page": main_page,
    "Research Papers": page_name,
    "tags": tag_finder
}

from update_cache import update_cache
update_cache()
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()