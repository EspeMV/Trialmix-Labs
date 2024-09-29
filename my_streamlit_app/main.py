import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

st.logo("trialmix labs blue icon.svg")
st.set_page_config(layout = 'wide')

st.image("trialmix labs blue logo.svg", width=140)
st.write("### Trialmix Labs - Researcher Dashboard")
st.write("# My Clinical Trials")
x = st.text_input("Search")
st.write(f"Your search: {x}")

data = pd.read_csv("trials.csv")

col1, col2 = st.columns([7,7])
container = st.container(border=True)
f0, f1, f2, f3 = col1.columns([2,2,3,3])
is_clicked = f0.button(" Filters ")
filter1 = f1.selectbox("", ["F&M", "F", "M"], label_visibility='collapsed')
filter2 = f2.date_input("", label_visibility='collapsed', disabled=False)
filter3 = f3.text_input("", label_visibility='collapsed', placeholder="area/type", disabled=True, key='11')

message = col1.container(height=400, border=True)
# print(data.columns)
# for row in data.rows(/):
for _, row in data.iterrows():
    # message.chat_message(f"row['title']")
    box = message.info(f"{row['title']}")
    c0, c1, c2, c3, c4, c5 = message.columns([1,5,1,3,1,6])
    c0.write(r"  ")
    c1.write(f"{row['age_range']} years old")
    c2.write("| ")
    c3.write(f"  {row['sex']}")
    c4.write("| ")
    c5.write(f"{row['date']}")
    #message.write("")
    message.divider()


# st.feedback("stars")
# st.toggle("Activate")

rightsection = col2.info("This is an information box!")
choice = rightsection.selectbox("Select one of your clinical trials", data['title'])
is_clicked = col2.button("Analyze data and generate comments")
# col2.info("Analysis of Data Collected from", choice)

if is_clicked:
    col2.info("Comments about the diversity of participants/volunteers will appear here. Trialmix Labs plans to implement Machine Learning algorithms to analyze the data stored (age, sex, and ethnicity) to detect over-/under-representation of different groups and other biases.")

