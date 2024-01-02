import streamlit as st

f = open("/home/cilab/teja/IITMResearch/research_papers/diffusion/ddpm.md", "r")

st.markdown(f.read())