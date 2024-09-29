import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

st.logo("trialmix labs blue icon.svg")

st.write("# Researcher Dashboard")
st.write("## My Clinical Trials")
x = st.text_input("Search")
st.write(f"Your search: {x}")

col1, col2 = st.columns([5,4])
container = st.container(border=True)
col2.button("Filters")

data = pd.read_csv("trials.csv")
message = col1.container(height=320, border=True)
# print(data.columns)
# for row in data.rows(/):
for _, row in data.iterrows():
    message.chat_message(row['title'])
    c0, c1, c2, c3, c4, c5 = message.columns([1,6,1,3,1,6])
    c0.write(r"  ")
    c1.write(f"{row['age_range']} years old")
    c2.write("| ")
    c3.write(f"  {row['sex']}")
    c4.write("| ")
    c5.write(f"{row['date']}")
    #message.write("")
    #message.divider()


# st.feedback("stars")
# st.toggle("Activate")

is_clicked = st.button("Generate suggestions")
# st.link_button("Profile", url="/profile")
