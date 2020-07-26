import streamlit as st
from PIL import Image
import altair as alt
import pandas as pd
import numpy as np
import folium


def write():
    st.title('Results & Conclusion')
    st.header('Factoring in Living Cost')
    st.markdown(
        '''<p style='text-align: justify; '>The final part of this project was to determine locations that were ideal in terms of adjusted 
        salary by factoring in city-specific living costs. Due to time constraints, we only comapred living cost data from with salary estimates 
        from the Software Engineering roles in cities with at least 5 job postings.</p>''',
        unsafe_allow_html=True)

    st.markdown('''Here's what the top cities with at least 5 Software Engineering jobs looked like:''')

    df = pd.read_csv('swe_cleaned.csv')
    count = df.groupby('City').count().reset_index()
    count = count[count.get('Rating') > 4] # Grab cities with more than 4 job postings
    unique_city = count.get('City').unique()

    st.code('''count = df.groupby('City').count().reset_index()
count = count[count.get('City') > 4] # Grab cities with more than 4 job postings
unique_city = count.get('City').unique()
unique_city''')
    st.text(
        '''array(['Annapolis Junction', 'Arlington', 'Blacksburg', 'Boston',
       'Burlington', 'Cedar Park', 'Chantilly', 'Charlotte', 'Chicago',
       'Chubbuck', 'Cincinnati', 'Edmond', 'Emeryville', 'Greensboro',
       'Herndon', 'Jacksonville', 'Kansas City', 'McLean', 'New York',
       'Omaha', 'Peoria Heights', 'Phoenix', 'Pleasanton', 'Reston',
       'Salt Lake City', 'San Diego', 'San Francisco', 'San Jose',
       'Seattle', 'Springfield', 'Sterling', 'Sunnyvale', 'Tempe',
       'Waltham', 'Washington'], dtype=object)''')

    st.markdown(
        '''We then proceeded to collect data on the living cost indices for each of the 35 cities listed from [BestPlaces.com](https://www.bestplaces.net/cost-of-living/)'''
    )

    st.code('''living_cost = pd.read_csv('living_cost.csv')
living_cost.head()''')

    living_cost = pd.read_csv('living_cost.csv')
    st.dataframe(living_cost.head())

    st.markdown('''The marker for comparison we chose was the average Software Engineering salary and miscellaneous living cost index of San Diego ''')

    df = df[df.get('City').isin(unique_city)]
    sd = df[df.get('City').str.contains('San Diego')]
    sd_avg = sd.get('AvgSalary').mean()
    sd_avg # Average Salary Estimate in San Diego
    sd_mc = 105.6 # From BetterPlaces.net
    living_cost = living_cost.set_index('city')

    st.code('''df = df[df.get('City').isin(uniquecity)]
sd = df[df.get('City').str.contains('San Diego')]
sd_avg = sd.get('AvgSalary').mean()
sd_avg # Average Salary Estimate in San Diego''')
    st.text('''82.16666666666667''')

    st.code('''sd_mc = 105.6 # Miscellaneous Living Cost Index from BetterPlaces.net
living_cost = living_cost.set_index('city')

def new_index(city):

        misc_index = df_lc.loc[city, 'misc_index']
        sd_misc = sd_mc
        misc_percent = round(((misc_index / sd_misc) - 1), 2)

        return misc_percent
    ''')

    

    st.code('''df['MC Difference'] = df.get('City').apply(new_index)
df.sort_values(by=['MC Difference'], ascending=False)''')
