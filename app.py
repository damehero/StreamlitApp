import streamlit as st
import pandas as pd
import numpy as np



st.title('STEM Career Project Exploration')
st.header('Tech jobs and Salaries across the United States')

st.markdown(
    'This is Web App is a modification of an assignment submitted as a final project for *COGS 108: Data Science in Practice* taught in Spring 2020.'
    + ' The original notebook repo can be viewed [here](https://github.com/damehero/COGS108_Repo/blob/master/FinalProject_group62.ipynb).'
)
st.markdown('This page is meant to serve as an interactive and visual walkthrough of the original project along with additional findings.')

st.header("'Software Engineering' jobs scraped from Glassdoor.com")
df = pd.read_csv('swe.csv')
st.dataframe(df.head())

st.latex('a^2 + b^2 = c^2')

activities = ["About", "Github"]
choice = st.sidebar.selectbox("Menu",activities)

