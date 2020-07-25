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


    df_geo = pd.read_csv('df_geo.csv')
    dsgn_geo = pd.read_csv('dsgn_geo.csv')
    data_geo = pd.read_csv('data_geo.csv')


    bubble_map = folium.Map(location=[37, -102], zoom_start=4)

    options = st.multiselect(
     'Select Job Postings',
     ['Software Engineering', 'Data Science', 'Product Design'])


    if 'Software Engineering' in options and 'Data Science' not in options and 'Product Design' not in options: #SWE only
        for i in range(len(df_geo)):
            folium.Circle(location=[df_geo.Lat.iloc[i], df_geo.Lon.iloc[i]],
                      popup=df_geo.Location.iloc[i],
                      radius=int(df_geo.Count.iloc[i]) * 10000,
                      color='#7551f8',
                      fill=True,
                      fill_color='#7551f8').add_to(bubble_map)
        st.markdown(bubble_map._repr_html_(),
                unsafe_allow_html=True)  # Allows Folium map to be displayed

    elif 'Data Science' in options and 'Software Engineering' not in options and 'Product Design' not in options: #DS only
        for i in range(len(data_geo)):
            folium.Circle(location = [data_geo.Lat.iloc[i], data_geo.Lon.iloc[i]],
                        popup = data_geo.Location.iloc[i],
                        radius = int(data_geo.Count.iloc[i]) *10000,
                        color ='#28CF17',
                        fill = True,
                        fill_color = '#28CF17').add_to(bubble_map)
        st.markdown(bubble_map._repr_html_(), unsafe_allow_html=True)

    elif 'Product Design' in options and 'Software Engineering' not in options and 'Data Science' not in options: #DSGN only
        for i in range(len(dsgn_geo)):
            folium.Circle(location = [dsgn_geo.Lat.iloc[i], dsgn_geo.Lon.iloc[i]],
                    popup = dsgn_geo.Location.iloc[i],
                    radius = int(dsgn_geo.Count.iloc[i]) *10000,
                    color ='#F85151',
                    fill = True,
                    fill_color = '#F85151').add_to(bubble_map)
        st.markdown(bubble_map._repr_html_(),
            unsafe_allow_html=True)  # Allows Folium map to be displayed

    elif 'Software Engineering' in options and 'Product Design' in options and 'Data Science' not in options:  #SWE & DSGN
        for i in range(len(df_geo)):
            folium.Circle(location=[df_geo.Lat.iloc[i], df_geo.Lon.iloc[i]],
                        popup=df_geo.Location.iloc[i],
                        radius=int(df_geo.Count.iloc[i]) * 10000,
                        color='#7551f8',
                        fill=True,
                        fill_color='#7551f8').add_to(bubble_map)

        for i in range(len(dsgn_geo)):
            folium.Circle(location=[dsgn_geo.Lat.iloc[i], dsgn_geo.Lon.iloc[i]],
                    popup=dsgn_geo.Location.iloc[i],
                    radius=int(dsgn_geo.Count.iloc[i]) * 10000,
                    color='#F85151',
                    fill=True,
                    fill_color='#F85151').add_to(bubble_map)
        st.markdown(bubble_map._repr_html_(),
                unsafe_allow_html=True)

    elif 'Software Engineering' in options and 'Data Science' in options and 'Product Design' not in options: #SWE & DATA
        for i in range(len(df_geo)):
            folium.Circle(location=[df_geo.Lat.iloc[i], df_geo.Lon.iloc[i]],
                          popup=df_geo.Location.iloc[i],
                          radius=int(df_geo.Count.iloc[i]) * 10000,
                          color='#7551f8',
                          fill=True,
                          fill_color='#7551f8').add_to(bubble_map)

        for i in range(len(data_geo)):
            folium.Circle(location=[data_geo.Lat.iloc[i], data_geo.Lon.iloc[i]],
                        popup=data_geo.Location.iloc[i],
                        radius=int(data_geo.Count.iloc[i]) * 10000,
                        color='#28CF17',
                        fill=True,
                        fill_color='#28CF17').add_to(bubble_map)
        st.markdown(bubble_map._repr_html_(), unsafe_allow_html=True)

    elif 'Data Science' in options and 'Product Design' in options and 'Software Engineering' not in options: #DATA & DSGN
        for i in range(len(data_geo)):
            folium.Circle(location=[data_geo.Lat.iloc[i], data_geo.Lon.iloc[i]],
                popup=data_geo.Location.iloc[i],
                radius=int(data_geo.Count.iloc[i]) * 10000,
                color='#28CF17',
                fill=True,
                fill_color='#28CF17').add_to(bubble_map)

        for i in range(len(dsgn_geo)):
            folium.Circle(location=[dsgn_geo.Lat.iloc[i], dsgn_geo.Lon.iloc[i]],
                popup=dsgn_geo.Location.iloc[i],
                radius=int(dsgn_geo.Count.iloc[i]) * 10000,
                color='#F85151',
                fill=True,
                fill_color='#F85151').add_to(bubble_map)
        st.markdown(bubble_map._repr_html_(), unsafe_allow_html=True)

    elif 'Software Engineering' in options and 'Data Science' in options and 'Product Design' in options:  #SWE & DATA & DSGN
        for i in range(len(df_geo)):
            folium.Circle(location=[df_geo.Lat.iloc[i], df_geo.Lon.iloc[i]],
                          popup=df_geo.Location.iloc[i],
                          radius=int(df_geo.Count.iloc[i]) * 10000,
                          color='#7551f8',
                          fill=True,
                          fill_color='#7551f8').add_to(bubble_map)

        for i in range(len(data_geo)):
            folium.Circle(
                location=[data_geo.Lat.iloc[i], data_geo.Lon.iloc[i]],
                popup=data_geo.Location.iloc[i],
                radius=int(data_geo.Count.iloc[i]) * 10000,
                color='#28CF17',
                fill=True,
                fill_color='#28CF17').add_to(bubble_map)

        for i in range(len(dsgn_geo)):
            folium.Circle(
                location=[dsgn_geo.Lat.iloc[i], dsgn_geo.Lon.iloc[i]],
                popup=dsgn_geo.Location.iloc[i],
                radius=int(dsgn_geo.Count.iloc[i]) * 10000,
                color='#F85151',
                fill=True,
                fill_color='#F85151').add_to(bubble_map)
        st.markdown(bubble_map._repr_html_(), unsafe_allow_html=True)

    else:
        st.markdown(bubble_map._repr_html_(),
        unsafe_allow_html=True)

    st.write('You selected:', options)




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
