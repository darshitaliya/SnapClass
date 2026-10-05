import streamlit as st


def footer_home():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by <span style="color:#white;">Darsh Italiya</span></p>
        </div>
        """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:#31333F;"> Created with ❤️ by <span style="color: black;">Darsh Italiya</span></p>
        </div>
        """, unsafe_allow_html=True)
