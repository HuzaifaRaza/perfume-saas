import streamlit as st
from supabase_client import supabase

def manage():
    st.title("Raw Materials")

    name = st.text_input("Material Name")
    unit = st.text_input("Unit")
    stock = st.number_input("Opening Stock", min_value=0.0)

    if st.button("Add Material"):
        supabase.table("raw_materials").insert({
            "name": name,
            "unit": unit,
            "stock_qty": stock
        }).execute()
        st.success("Material added")

    data = supabase.table("raw_materials").select("*").execute().data
    st.dataframe(data)

