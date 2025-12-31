import streamlit as st

def require_login():
    if not st.session_state.get("logged_in"):
        st.warning("Please login")
        st.stop()

def require_role(roles):
    if st.session_state.get("role") not in roles:
        st.error("Access denied")
        st.stop()

