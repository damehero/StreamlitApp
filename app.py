import streamlit as st 
import pandas as pd
import numpy as np


st.title('STEM Career Project')
st.header('Tech jobs and salaries across the United States')

st.markdown('This is project was originally submitted as ')
st.latex('a^2 + b^2 = c^2')

activities = ["About", "Github"]
choice = st.sidebar.selectbox("Menu",activities)

