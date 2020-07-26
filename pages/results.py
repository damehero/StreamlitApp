import streamlit as st
from PIL import Image
import altair as alt
import pandas as pd
import numpy as np
import folium


def write():
    st.title('Results & Conclusion')
    st.header('Factoring in Living Cost')
    st.markdown('''The final part of this project was to determine locations that were ideal in terms of adjusted salary by factoring in living costs.''')