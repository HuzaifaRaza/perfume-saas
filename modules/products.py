import streamlit as st
from supabase_client import supabase

def manage():
    st.title("Products")

    name = st.text_input("Perfume Name")
    sku = st.text_input("SKU")
    price = st.number_input("Sale Price", min_value=0.0)

    if st.button("Add Product"):
        supabase.table("products").insert({
            "name": name,
            "sku": sku,
            "sale_price": price
        }).execute()
        st.success("Product added")

    data = supabase.table("products").select("*").execute().data
    st.dataframe(data)

