import bcrypt
import streamlit as st
from supabase_client import supabase

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def login():
    st.title("Perfume SaaS Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        res = supabase.table("users").select("*") \
            .eq("username", username).eq("is_active", True).execute()

        if not res.data:
            st.error("Invalid credentials")
            return

        user = res.data[0]

        if verify_password(password, user["password_hash"]):
            st.session_state.logged_in = True
            st.session_state.user_id = user["id"]
            st.session_state.role = user["role"]
            st.rerun()
        else:
            st.error("Invalid credentials")

def logout():
    if st.button("Logout"):
        st.session_state.clear()
        st.rerun()

