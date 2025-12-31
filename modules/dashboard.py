import streamlit as st
from supabase_client import supabase

def show():
    st.title("Dashboard")

    products = supabase.table("products").select("*").execute().data
    raw = supabase.table("raw_materials").select("*").execute().data

    st.metric("Total Perfumes", len(products))
    st.metric("Raw Materials", len(raw))

