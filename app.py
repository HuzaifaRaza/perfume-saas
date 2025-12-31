import streamlit as st
from auth import login, logout
from permissions import require_login
from modules import dashboard, users, products, raw_materials

st.set_page_config(page_title="Perfume SaaS", layout="wide")

if not st.session_state.get("logged_in"):
    login()
else:
    st.sidebar.title("Menu")

    menu = st.sidebar.selectbox(
        "Navigate",
        ["Dashboard", "Users", "Products", "Raw Materials"]
    )

    logout()

    require_login()

    if menu == "Dashboard":
        dashboard.show()
    elif menu == "Users":
        users.manage()
    elif menu == "Products":
        products.manage()
    elif menu == "Raw Materials":
        raw_materials.manage()

