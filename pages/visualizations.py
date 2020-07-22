import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plot

df = pd.read_csv('swe_cleaned.csv')
df_cat = df[[
    'Location', 'Size', 'Type of ownership', 'Industry', 'Sector', 'State',
    'Seniority'
    ]]

def write():
    st.write('VIZ')

    cat_num = df_cat['Type of ownership'].value_counts()
    print("Graph for Ownership Type: unique =", (len(cat_num)))
    chart = sns.barplot(y=cat_num.index, x=cat_num)
    chart.set_yticklabels(chart.get_yticklabels())
    st.pyplot(bbox_inches="tight")

    cat_num = df_cat['Size'].value_counts()
    print("Graph for Company Size: unique =", (len(cat_num)))
    chart = sns.barplot(y=cat_num.index, x=cat_num)
    chart.set_yticklabels(chart.get_yticklabels())
    st.pyplot(bbox_inches="tight")
