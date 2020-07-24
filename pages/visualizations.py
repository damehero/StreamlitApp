import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plot
import altair as alt
import folium

df = pd.read_csv('swe_cleaned.csv')
df_cat = df[[
    'Location', 'Size', 'Type of ownership', 'Industry', 'Sector', 'State',
    'Seniority'
    ]]

def write():
    st.title('Data Visualizations')
    st.header('Graphs and Maps of the Data')

    st.markdown(
        '''<p style='text-align: justify; '>This page serves as a display for all of the graphs I generated from the dataset as well as mappings.</p>''',
        unsafe_allow_html=True)


    bubble_map = folium.Map(location=[37, -102], zoom_start=4)

    df_geo = pd.read_csv('df_geo.csv')

    option = st.selectbox(
     'Choose a display',
     ('Blank', 'Locations'))

    if option == 'Locations':
        for i in range(len(df_geo)):
            folium.Circle(location=[df_geo.Lat.iloc[i], df_geo.Lon.iloc[i]],
                      popup=df_geo.Location.iloc[i],
                      radius=int(df_geo.Count.iloc[i]) * 10000,
                      color='#7551f8',
                      fill=True,
                      fill_color='#7551f8').add_to(bubble_map)

        st.markdown(bubble_map._repr_html_(),
                unsafe_allow_html=True)  # Allows Folium map to be displayed

    elif option == 'Blank':
        st.markdown(bubble_map._repr_html_(),
                unsafe_allow_html=True)

    st.write('You selected:', option)


    





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

    cat_num = df_cat['Industry'].value_counts()
    print("Graph for Industry: unique =", (len(cat_num)))
    plot.figure(figsize=(10, 10))
    chart = sns.barplot(y=cat_num.index, x=cat_num)
    chart.set_yticklabels(chart.get_yticklabels())
    st.pyplot(bbox_inches="tight")
