import streamlit as st
import profile

st.logo("trialmix labs blue logo.svg")

st.write("# Trial Analysis")

import pandas as pd
import numpy as np
from io import StringIO

trial_name = st.text_input("Trial Name")

uploaded_file = st.file_uploader("Upload a CSV file of the trial participants", type=['csv'], accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

data = pd.read_csv("participants.csv")

if uploaded_file:
    # Loading the data from csv file
    data = pd.read_csv(uploaded_file)
    st.write(data)
else:
    st.write("No data available.")

## is_clicked = col1.button("Trial 1 \n A bit of information about the trial number 1 and other specs")

# st.toggle("Activate")

is_clicked = st.button("Analyze data and identify lack of/over representation or biases")