import streamlit as st

st.logo("trialmix labs blue icon.svg")
st.set_page_config(layout = 'centered')

st.write("# Profile")

role = "client"

p1, p2 = st.columns([1,1])
first_name = p1.text_input("First name")
last_name = p2.text_input("Last name")
# p1.write("Full name:", first_name, last_name)

role = p1.selectbox("Account type", ["Client", "User", "Admin"], disabled=True, placeholder="client")
age = p2.number_input("Age", 0, 110)

is_clicked = p1.button("Save information")

# if is_clicked: