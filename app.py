"""
Welcome page :
This welcome page is the default page of our application.
It consits in an image tutorial and a usage example to guide our users, embeded in a html file
"""

import os
import requests
import streamlit as st
import subprocess

from src.application.recipe_finder_functions import display_html_in_streamlit
from src.authentification.auth_ui import login_form, show_user_panel

# Add a title to the page_title
st.set_page_config(layout="wide", page_title='FRIDGE & COOK', initial_sidebar_state='collapsed', page_icon="🍴")

if "flask_started" not in st.session_state:
    subprocess.Popen(["python", "src/authentification/login_api.py"])
    st.session_state.flask_started = True

if "status_message" in st.session_state:
    st.success(st.session_state.status_message)
    del st.session_state.status_message  # Clear after showing once

# Load Welcome page.html with the corresponding styling of the page
HTML_FILE_PATH = "assets/html/Welcome_Page.html"
CSS_FILE_PATH = "assets/css/style_welcome.css"

# Check if the file exists before attempting to display it
if os.path.exists(HTML_FILE_PATH):
    _, col1, col2, _ = st.columns([2, 1, 1, 2])
    if col1.button("🔎 Recipe Finder"):
        st.switch_page("pages/recipe_finder_page.py")
    # if col2.button("🥗 Recipe Page"):
    #     st.switch_page("pages/recipe_page.py")
    display_html_in_streamlit(HTML_FILE_PATH, CSS_FILE_PATH, height=2700, width=1080)
else:
    st.error(f"The HTML file '{HTML_FILE_PATH}' does not exist. Please check the path.")




# Show login form if user not logged in
if not st.session_state.get("logged_in"):
    login_form()
else:
    show_user_panel()  # only shows user info and logout button
    st.write("🎉 Welcome back!")