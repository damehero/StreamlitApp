import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from PIL import Image
import matplotlib.pyplot as plot
import altair as alt
import folium

#Data Imports
df_geo = pd.read_csv('df_geo.csv')
dsgn_geo = pd.read_csv('dsgn_geo.csv')
data_geo = pd.read_csv('data_geo.csv')

def write():
    st.title('Data Visualizations')
    st.header('Graphs and Maps of the Data')

    st.markdown(
        '''<p style='text-align: justify; '>Below are a few of the charts that were generated from various labels in the three datasets.</p>''',
        unsafe_allow_html=True)

    bubble_map = folium.Map(location=[37, -102], zoom_start=4)
    st.subheader('Bubble Map Overlays')

    options = st.multiselect(
    'Select Job Type(s)',
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

    st.write('')
    st.write(
        'Where the radius of each bubble corresponds to the number of postings at that location.'
    )
    image1 = Image.open('images/swe_color.png')
    image2 = Image.open('images/data_color.png')
    image3 = Image.open('images/dsgn_color.png')

    st.image([image1, image2, image3], caption = ['SWE', 'DATA', 'DSGN'])



    st.subheader('Categorical Bar Charts')
    option = st.selectbox(
        'Select Job Type',
        ('Software Engineering', 'Data Science', 'Product Design'))

    st.write('You selected:', option)

    if option == 'Software Engineering':

        df = pd.read_csv('swe_cleaned.csv')

        df_cat = df[[
            'Location', 'Size', 'Type of ownership', 'Industry', 'Sector',
            'State', 'Seniority']]

        st.markdown('**States**')
        cat_num = df_cat['State'].value_counts()
        st.write("Chart for State: unique =", (len(cat_num)))
        plot.figure(figsize=(10,10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown('**Industry**')
        cat_num = df_cat['Industry'].value_counts()
        st.write("Chart for Industry: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown('**Sector**')
        cat_num = df_cat['Sector'].value_counts()
        st.write("Chart for Sector: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown('**Company Size**')
        cat_num = df_cat['Size'].value_counts()
        st.write("Chart for Company Size: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown('**Type of Ownership**')
        cat_num = df_cat['Type of ownership'].value_counts()
        st.write("Chart for Ownership Type: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

    elif option == 'Data Science':

        df2 = pd.read_csv('data.csv')

        non_state_ab = df2[(df2['State'] == 'United States') |
                           (df2['State'] == 'Virginia') |
                           (df2['State'] == 'California') |
                           (df2['State'] == 'New York State') |
                           (df2['State'] == 'Remote')].index
        df2 = df2.drop(non_state_ab)
        df2 = df2.replace(to_replace='-1', value="Unknown")

        df_cat = df2[[
            'Location', 'Size', 'Type of ownership', 'Industry', 'Sector',
            'State']]

        st.markdown('**States**')
        cat_num = df_cat['State'].value_counts()
        st.write("Chart for State: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown('**Industry**')
        cat_num = df_cat['Industry'].value_counts()
        st.write("Chart for Industry: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown('**Sector**')
        cat_num = df_cat['Sector'].value_counts()
        st.write("Chart for Sector: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown('**Company Size**')
        cat_num = df_cat['Size'].value_counts()
        st.write("Chart for Company Size: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown('**Type of Ownership**')
        cat_num = df_cat['Type of ownership'].value_counts()
        st.write("Chart for Ownership Type: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

    elif option == 'Product Design':

        df3 = pd.read_csv('dsgn.csv')

        non_state_ab = df3[(df3['State'] == 'United States') |
                           (df3['State'] == 'Chicago') |
                           (df3['State'] == 'New Jersey') |
                           (df3['State'] == 'Arkansas') |
                           (df3['State'] == 'North Carolina') |
                           (df3['State'] == 'Remote')].index
        df3 = df3.drop(non_state_ab)
        df3 = df3.replace(to_replace='-1', value="Unknown")

        df_cat = df3[[
            'Location', 'Size', 'Type of ownership', 'Industry', 'Sector',
            'State']]

        st.markdown('**States**')
        cat_num = df_cat['State'].value_counts()
        st.write("Chart for State: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown('**Industry**')
        cat_num = df_cat['Industry'].value_counts()
        st.write("Chart for Industry: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown('**Sector**')
        cat_num = df_cat['Sector'].value_counts()
        st.write("Chart for Sector: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown('**Company Size**')
        cat_num = df_cat['Size'].value_counts()
        st.write("Chart for Company Size: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown('**Type of Ownership**')
        cat_num = df_cat['Type of ownership'].value_counts()
        st.write("Chart for Ownership Type: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")