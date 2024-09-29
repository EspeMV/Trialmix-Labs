import streamlit as st

st.logo("trialmix labs blue icon.svg")
st.set_page_config(layout = 'wide')

st.write("# Profile")

role = "client"
age = st.number_input("Age", 0, 110)

first_name = st.text_input("Edit name")
st.write("Name:",first_name)