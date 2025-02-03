import streamlit as st
# import requests
# from bs4 import BeautifulSoup

 
# Add images for branding
st.image("./assets/Untitled17_20250113001924.png", width=400)
st.sidebar.image("./assets/reshot-icon-flowers-in-the-branch-QXUYA35D8W.svg", width=180)
 
# Sidebar navigation
page = st.sidebar.radio("", ["About", "Shop", "ChatBot"])
 
if page == "About":
    st.title("SAKURA Online Shop")
    st.write("Welcome to our world!")

