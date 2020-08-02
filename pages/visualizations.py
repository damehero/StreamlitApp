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

        st.markdown(
            ''' <p style='text-align: justify; '>From our job data, a total of 42/50 states are represented in the listings. 
            An interesting feature of this bar chart is that Virginia had more total listings than California, indicating that 
            there is a high demand for software engineers currently unfulfilled.</p>''',
            unsafe_allow_html=True)

        st.markdown('**Industry**')
        cat_num = df_cat['Industry'].value_counts()
        st.write("Chart for Industry: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown(
            ''' <p style='text-align: justify; '>This next bar chart shows the dispersion of jobs across various types of industries. 
            Again, it comes as no surprise that a large portion of software engineering jobs are listed in industries related to tech 
            such as Computer Hardware, Enterprise Software, Internet, and IT Services. Something that was surprising, however, is how 
            wide the spread of industries is as it spans some uncommon domains for traditional software engieering such as Religious 
            Organizations, Pharmaceuticals, and Manufacturing.
            </p>''',
            unsafe_allow_html=True)

        st.markdown('**Sector**')
        cat_num = df_cat['Sector'].value_counts()
        st.write("Chart for Sector: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown(
            ''' <p style='text-align: justify; '>Sector, different from Industry, describes a larger segment of the economy. 
            Overwhelmingly, the majority of software engineering jobs fall into the cateogry of Information Technology.
            </p>''',
            unsafe_allow_html=True)

        st.markdown('**Company Size**')
        cat_num = df_cat['Size'].value_counts()
        st.write("Chart for Company Size: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown(
            ''' <p style='text-align: justify; '>This bar chart shows the spread of company sizes within our data. 
            We can see that the majority of companies with open listings fall into the mid-size range with between 
            51 to 200 and 201 to 500 employees.
            </p>''',
            unsafe_allow_html=True)

        st.markdown('**Type of Ownership**')
        cat_num = df_cat['Type of ownership'].value_counts()
        st.write("Chart for Ownership Type: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown(
            ''' <p style='text-align: justify; '>This bar chart reveals the type of ownership amongst the companies in the job data. 
            Unsurprisingly, the majority of companies are private, followed by a few public companies and nonprofits.
            </p>''',
            unsafe_allow_html=True)

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

        st.markdown(
            ''' <p style='text-align: justify; '>There are just 35 unique states represented in the Data Science job postings, 
            the smallest variety of all 3 jobs types (just 1 lower than Design). The majority of jobs are located on the coasts.
            </p>''',
            unsafe_allow_html=True)

        st.markdown('**Industry**')
        cat_num = df_cat['Industry'].value_counts()
        st.write("Chart for Industry: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown(
            ''' <p style='text-align: justify; '>An interesting and unexpected feature of the Data Science data can be seen in this bar chart. 
            The main industry for Data Science in the US appears to be in Biotech and Pharmaceuticals. Given the boom in bioengineering technologies 
            over the last two decades, this seems to make sense although I certainly didn't expect this industry to top the list. Having specific 
            domain knowledge in the biological sciences could greatly increase the chances of landing a job in Data Science.
            </p>''',
            unsafe_allow_html=True)

        st.markdown('**Sector**')
        cat_num = df_cat['Sector'].value_counts()
        st.write("Chart for Sector: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown(
            ''' <p style='text-align: justify; '>While the main industry for Data Science was in Biotech, the combination of IT Services and Computer Hardware/Software industries are enough to top the list of sectors.
            </p>''',
            unsafe_allow_html=True)

        st.markdown('**Company Size**')
        cat_num = df_cat['Size'].value_counts()
        st.write("Chart for Company Size: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown(
            ''' <p style='text-align: justify; '>It seems that mid-range and slightly larger mid-range companies dominate the space of Data Science job postings. 
            I would've guessed that larger companies would be at the top of this bar chart since I'd assume they may have more data from various products/services/departments.
            </p>''',
            unsafe_allow_html=True)

        st.markdown('**Type of Ownership**')
        cat_num = df_cat['Type of ownership'].value_counts()
        st.write("Chart for Ownership Type: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown(
            ''' <p style='text-align: justify; '>Again, unsurprisingly, private companies dominate the job listings. 
            This seems to be a trend amongst all the charts as sites such as Glassdoor are generally used by private 
            companies as opposed non-profits or government organizations.
            </p>''',
            unsafe_allow_html=True)

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

        st.markdown(
            ''' <p style='text-align: justify; '>The locations of Design jobs on Glassdoor are by far the most skewed out of all 3 job types 
            with the overwhelming majority being located in California.
            </p>''',
            unsafe_allow_html=True)

        st.markdown('**Industry**')
        cat_num = df_cat['Industry'].value_counts()
        st.write("Chart for Industry: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown(
            ''' <p style='text-align: justify; '>An interesting aspect of the Design data is that the number 1 industry listed is for Agriculture and Eningeering Services. 
            This was particularly curious to me. After doing some research I found that these Design jobs are as civil, structural, and geotechnical design engineers.
            </p>''',
            unsafe_allow_html=True)

        st.markdown('**Sector**')
        cat_num = df_cat['Sector'].value_counts()
        st.write("Chart for Sector: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown(
            ''' <p style='text-align: justify; '>The IT space dominates as the main sector once again, being a combination of Computing and IT. 
            A unique aspect of this bar chart is that Business Services are a much closer second for Design roles in comparison to Software Engineering or Data Science.
            </p>''',
            unsafe_allow_html=True)

        st.markdown('**Company Size**')
        cat_num = df_cat['Size'].value_counts()
        st.write("Chart for Company Size: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown(
            ''' <p style='text-align: justify; '>Smaller mid-range to mid-range companies are the top ones listed as hiring, similar to the Software Engineering Data. 
            Designers bring value to companies of all sizes.
            </p>''',
            unsafe_allow_html=True)

        st.markdown('**Type of Ownership**')
        cat_num = df_cat['Type of ownership'].value_counts()
        st.write("Chart for Ownership Type: unique =", (len(cat_num)))
        plot.figure(figsize=(10, 10))
        chart = sns.barplot(y=cat_num.index, x=cat_num)
        chart.set_yticklabels(chart.get_yticklabels())
        st.pyplot(bbox_inches="tight")

        st.markdown(
            ''' <p style='text-align: justify; '>Finally, there's no surprise here as the top companies hiring on Glassdoor are once again privately owned. 
            There is however, a larger appearance of School/School Districts on this bar chart in comparison to the other 2 job types.
            </p>''',
            unsafe_allow_html=True)