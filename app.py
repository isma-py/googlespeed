import os
import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="Google Meet Clone",
    page_icon="📹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit UI elements for full-screen view
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        header {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        [data-testid="stHeader"] {display: none !important;}
        iframe {
            width: 100% !important;
            height: 100vh !important;
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# Read HTML code from index.html
html_file_path = os.path.join(os.path.dirname(__file__), "index.html")

if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        meet_html_code = f.read()
    
    # Render with explicit camera, microphone, and display-capture iframe permissions
    components.html(meet_html_code, height=800, scrolling=False)
else:
    st.error("Error: index.html file not found in the root directory!")