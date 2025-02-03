import streamlit as st
# import requests
# from bs4 import BeautifulSoup

 
# Add images for branding

 
# Sidebar navigation
page = st.sidebar.radio("", ["About", "Shop", "ChatBot"])
 
if page == "About":
    st.title("SAKURA Online Shop")
    st.write("Welcome to our world!")

