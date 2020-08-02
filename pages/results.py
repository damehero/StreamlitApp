import streamlit as st
from streamlit_folium import folium_static
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

    st.markdown(
        '''<p style='text-align: justify; '>Our formula for finding these 'ideal' locations was to identify cities that have a lower <b>Miscellaneous Cost Index</b> 
        than San Diego (our point of comparison) as well as have a higher <b>Average Salary</b>. <a href="https://www.bestplaces.net/">BestPlaces.net</a> defines Micellaneous Cost Index as "The cost index of those 
        goods and services not included in the other cost of living categories, including clothing, restaurants, repairs, entertainment, and other services." We decided that 
        this was a good metric of measurement since it gages money leftover after essential living costs (i.e. pocket money).</p>''',
        unsafe_allow_html=True)

    st.markdown('''Here's what the top cities with at least 5 Software Engineering job postings looked like:''')

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
        '''After identifying these candidate cities, we proceeded to collect data on the Living Cost indices for each of the 35 cities listed above from [BestPlaces.net](https://www.bestplaces.net/cost-of-living/)'''
    )

    st.code('''living_cost = pd.read_csv('living_cost.csv')
living_cost.head()''')

    living_cost = pd.read_csv('living_cost.csv')
    st.dataframe(living_cost.head())

    st.markdown(
        '''The function below then calculates the *Micellaneous Percent Change Index* between San Diego and the other top cities based on the data from BestPlaces.
    ''')

    st.code('''sd_mc = 105.6 # Miscellaneous Living Cost Index of San Diego
living_cost = living_cost.set_index('city')

def new_index(city):

        misc_index = df_lc.loc[city, 'misc_index']
        sd_misc = sd_mc
        misc_percent = round(((misc_index / sd_misc) - 1), 2)

        return misc_percent
    ''')

    st.markdown('''After applying our function, we got a ranked percentage differential for each of the cities and plotted them on a horizontal bar chart for comparison.''')

    st.code('''df['MC Difference'] = df.get('City').apply(new_index)

new_df = pd.DataFrame({'count' : df.groupby( [ "City", "mc_diff"] ).size()}).reset_index().sort_values('mc_diff', ascending = False)
dataFrame = pd.DataFrame(data = new_df);

dataFrame.plot.barh(x = 'City', y = 'mc_diff', title = "Miscellaneous Cost Index Percent Change", color='#7DD7A7', figsize=(9,9));
plot.show(block = True)''')

    st.image(Image.open('images/misc_graph.png'),
             use_column_width=True)
    st.markdown(
        '''<p style='text-align: justify; '>As we can see, San Diego, Palo Alto, and Washington all have the same Miscellaneous Cost Index as there is zero change between them. Cities with lower Miscellaneous Costs have 
        negative change are showm on the top half of the chart while cities with greater Miscellaneous Cost have postive change and are on the bottom of the graph. The Miscellaneous 
        Cost Index is one metric reflective of how expensive it is to live in each city. Our percent change measures this cost with respect to San Diego.</p>''',
        unsafe_allow_html=True)

    st.markdown('''The final part of this procedure is to compare the cities that scored a low percentage change with the Average Salary of San Diego.''')

    st.code(
        '''avg_sal = df_sal_grouped.groupby('City').mean().reset_index().sort_values(by = 'AvgSal', ascending = False)
df_cost = avg_sal.merge(df_lc, left_on = 'City', right_on = 'city')
winners = df_cost[(df_cost.get('AvgSal') > 82) & (df_cost.get('misc_index') < 104) & (df_cost.get('count') > 6)].reset_index()

    ''')

    df_geo = pd.read_csv('df_geo.csv')
    df_winners = df_geo[df_geo['Location'].isin([
        'Blacksburg, VA', 'Cincinnati, OH', 'Peoria Heights, IL', 'Edmond, OK',
        'Tempe, AZ', 'Tallahassee, FL', 'Cedar Park, TX', 'Greensboro, NC',
        'Kansas City, MO', 'Salt Lake City, UT', 'Phoenix, AZ', 'Omaha, NE',
        'Chubbuck, ID'
    ])]

    bubble_map = folium.Map(location=[37, -102], zoom_start=4)

    for i in range(len(df_winners)):
        folium.Circle(
            location=[df_winners.Lat.iloc[i], df_winners.Lon.iloc[i]],
            popup=df_winners.Location.iloc[i],
            radius=100000,
            color='#7DD7A7',
            fill=True,
            fill_color='#7DD7A7').add_to(bubble_map)
    folium_static(bubble_map)

    st.markdown('')
    st.markdown(
        '''<p style='text-align: justify; '>This Bubble Map shows the 'ideal' locations overlayed ontop of the previous map which showed job posting frequency. 
        Each green dot represents a city which satisfies all 3 conditions:
        <ol>
  <li>Average Salary Estimae Greater than $82k (San Diego's Average Salary Estimate for Software Engineers)</li>
  <li>Miscellaneous Cost Index Less than 104 (San Diego's Miscellaneous Cost Index)</li>
  <li>At least 5 Postings (The number of job listings in San Diego)</li>
</ol></p>''',
        unsafe_allow_html=True)

    st.header('Conclusion & Discussion')
    st.markdown(
        '''<p style='text-align: justify; '>After web-scraping Glassdoor and plotting our data visualizations, we took a look at the cities that 
        had more job listings, lower miscellaneous index, and higher average salary than San Diego, and found best cities to live in as a Software Engineer 
        currently residing in San Diego but hoping to relocate are:</p>''',
        unsafe_allow_html=True)

    st.image(Image.open('images/cities.png'),
             caption="'Winning Locations' for Software Engineers",
             use_column_width=True)


    st.markdown('''<p style='text-align: justify; '>We were most surprised that we did not see any cities in the California Bay Area on this list, due to their higher miscellaneous cost index. 
This means that although the region in Silicon Valley offers a higher salary and more job postings compared to San Diego, it still is not the “perfect” place to live because people 
have less to spend on miscellaneous, non-essential costs like entertainment, restaurants, and clothing. By looking at miscellaneous cost index, we were able to see that typical tech-job 
alluring cities like San Francisco, Los Angeles, New York were not always the best places to live. Some limitations that we saw in our project included the amount of Glassdoor entries we 
were able to scrape and salary estimates instead of exact salary amounts.</p>''',
        unsafe_allow_html=True)


    st.markdown(
        '''<p style='text-align: justify; '>Revisiting our hypothesis, we were able to successfully predict that the best cities for Computer Science related careers/majors will be the 
        cities with the most job listings, lowest miscellaneous/non-essential costs, and highest average salary (all relative to San Diego). However, our previous assumption about expecting 
        to only see cities near Northern California as the best cities to live in turned out to be proved wrong, as we see in the above list that none of those cities are located there.</p>''',
        unsafe_allow_html=True)

    st.markdown(
        '''<p style='text-align: justify; '>This analysis would be very resourceful for those individuals who are on a job search especially after being affected by the COVID-19 pandemic. 
        Our algorithm helps job seekers, primarily, fresh graduates of Computer Science related degrees to identify the most optimal location to work at, focusing on their income and job status.</p>''',
        unsafe_allow_html=True)


    st.info(
        ''' by: [Daman Heer](https://damehero.github.io/) | source: [GitHub](https://github.com/damehero/StreamlitApp) '''
    )