import streamlit as st
import bcrypt
from supabase_client import supabase
from permissions import require_role

def manage():
    require_role(["admin"])
    st.title("User Management")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["admin", "accountant", "production", "sales"])

    if st.button("Create User"):
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        supabase.table("users").insert({
            "username": username,
            "password_hash": hashed,
            "role": role
        }).execute()
        st.success("User created")

