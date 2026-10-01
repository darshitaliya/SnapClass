import streamlit as st
import base64
from pathlib import Path


def _logo_b64(filename):
    logo_path = Path(__file__).parent.parent.parent / "assets" / filename
    return base64.b64encode(logo_path.read_bytes()).decode()


def footer_home():
    logo = _logo_b64("darsh_italiya_logo.jpg")
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>  
        <img src='data:image/jpeg;base64,{logo}' style='max-height:25px; border-radius:4px;' />
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo = _logo_b64("dashboard_logo.png")
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:black;"> Created with ❤️ by </p>  
        <img src='data:image/png;base64,{logo}' style='max-height:25px; border-radius:4px;' />
        </div>
                
                """, unsafe_allow_html=True)
