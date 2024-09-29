import streamlit as st

st.logo("trialmix labs blue logo.svg")

st.write("# Profile")

role = "client"
age = st.number_input("Age", 0, 110)

first_name = st.text_input("Edit name")
st.write("Name:",first_name)