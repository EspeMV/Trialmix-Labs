import streamlit as st
import profile
import pandas as pd
import csv

st.logo("trialmix labs blue icon.svg")
st.set_page_config(layout = 'wide')

FILEPATH = r'C:\Users\maria_nsinvd8\Documents\GitHub\folder\Tech-Nova-Hack\my_streamlit_app\trials.csv'

st.write("# Add New Trial")

# if "trial_name" not in st.session_state:
#     st.session_state.trial_name = ""

import pandas as pd
import numpy as np
from io import StringIO


# container = st.empty()

# trial_age  = st.empty()
# trial_sex  = st.empty()
# trial_date = st.empty()
# placeholder = st.empty()


# global trial_age, trial_sex, trial_date
def save_info():
    # df = pd.DataFrame({
    #     'Name'
    # })
    #title,age_range,sex,date

    trial_name = st.session_state.trial_name
    trial_age = st.session_state.trial_age
    trial_sex = st.session_state.trial_sex
    trial_date = st.session_state.trial_date

    # df = pd.read_csv(FILEPATH)
    # df.loc[len(df)] = [
    #         trial_name,
    #         trial_age, 
    #         trial_sex, 
    #         trial_date
    #     ]

    # print(df)
    # df.to_csv(FILEPATH)

    with open(FILEPATH, 'a') as f:
        # global trial_age, trial_sex, trial_date
        csv_writer = csv.writer(f)
        print(trial_age, trial_sex, trial_date)
        csv_writer.writerow([
            trial_name,
            trial_age, 
            trial_sex, 
            trial_date
        ])



# with placeholder.container():
#     global trial_age, trial_sex, trial_date
#     trial_age = st.text_input("Age Range", key='1')
#     trial_sex = st.text_input("Sex (F, M or F&M)", key='2')
#     trial_date = st.text_input("Date of trial (mm/dd)", key='3')
#     st.toggle("Make public")
# is_clicked = st.button("Save", on_click=save_info, key='4')

# trial_age.text_input("Age Range", key='1')
# trial_sex.text_input("Sex (F, M or F&M)", key='2')
# trial_date.text_input("Date of trial (mm/dd)", key='3')

st.text_input("Research Title/Trial Name", key='trial_name')
st.text_input("Age Range (min-max)", key='trial_age')
st.selectbox("Participants' Sex", ["F&M", "F", "M"], key='trial_sex')
st.date_input("Date of trial", key='trial_date')
st.toggle("Make public")

st.button("Save", on_click=save_info, key="button")


# st.link_button("Profile", url="/profile")


