import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

st.write("# Researcher Portal")

uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'], accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
# Loading the data from csv file
data = pd.read_csv("movies.csv")
st.write(data)

# Showing data in a graph
chart_data = pd.DataFrame(
np.random.randn(85, 2),
columns=["male", "female"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)

x = st.text_input("Favourite Movie?")
st.write(f"Your favourite movie is: {x}")

is_clicked = st.button("Click Me")
st.link_button("Profile", url="/profile")

st.write("## This is a H2 Title!")
