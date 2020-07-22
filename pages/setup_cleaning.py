import streamlit as st
from PIL import Image
import altair as alt
import pandas as pd
import numpy as np
import folium


def write():
    
    st.title(':computer: STEM Career Project Exploration')
    st.header('Tech jobs and Salaries across the United States')

    st.markdown(
        '''This is Web App is a modified expansion on an assignment orignially submitted as a final project for *COGS 108: Data Science in Practice*, 
        taught remotely at UC San Diego in Spring 2020. The old repository and data can be viewed [here](https://github.com/damehero/COGS108_Repo/blob/master/FinalProject_group62.ipynb).'''
    )
    st.markdown(
        'The goal of this page is to serve as an interactive and visual expansion to the original notebook.'
    )

    st.header('Setup')
    st.markdown('Relevant libraries for data cleaning and exploration.')
    import_code = '''
    import numpy as np
    import pandas as pd
    import altair as alt
    import seaborn as sns
    import matplotlib.pyplot as plot
    import googlemaps
    import folium'''
    st.code(import_code, language='python')

    st.header('Web Scraping Glassdoor')
    st.markdown(
        '''Follwing this great [Medium article](https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905) 
        on web scraping using *Selenium*, I was able to run a script to scrape 1000 unique job postings on Glassdoor.com. The author's original code 
        needed a few tweaks to run as the format of some of the HTML elements on the Glassdoor site had changed.'''
    )
    st.image(Image.open('images/scraper.png'),
             caption="'Software Engineering' query with no location specified",
             use_column_width=True)
    st.write('''
    I made the following three queries for: **Sofware Engineering**, **Data Scientist**, and **Designer** --all without specifiying a worksite location to get a wide range of positions across the United States.
    With each job entry, I collected the following information:''')
    st.image(Image.open('images/bullet.png'), use_column_width=True)

    st.markdown(
        '''Here's what the head of the DataFrame for *Software Engineering* jobs looked like after scraping:'''
    )
    st.code('''df = pd.read_csv('swe.csv')
df.head()
    ''',
            language='python')
    df = pd.read_csv('swe.csv')
    st.dataframe(df.head())

    st.header('Data Cleaning')
    st.write(
        '''After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:
    - Identified the *Seniority* of each job based on title listing
    - Parsed numeric data out of the *Salary Estimate* column
        - Removed rows with missing salaries
    - Made new columns for the Job *State* and *City*
        - Reverse geocoded locations using [Google Maps Cloud API](https://cloud.google.com/maps-platform/maps) (retrieve Latitude/Longitude)'''
    )

    st.write('''Here are what the some of these steps looked like:''')

    st.subheader('Identifying Seniority')
    st.code(
        '''unique_jobs = df['Job Title'].unique() # Overview of unique job titles
unique_jobs[0:5] # Sample of first 5 titles''',
        language='python')
    unique_jobs = df['Job Title'].unique()
    st.text(unique_jobs[0:5])
    st.markdown(
        '''From the *Job Title* column we find that there are 173 unique job titles with various levels of seniority. 
    The function below extracts the most common labels for senior and junior positions.'''
    )
    st.code('''def seniority(title):
    ''Identify and group specific job titles''
    title = title.lower().strip()
    seniority = ['senior', 'sr.', 'sr', 'lead', 'expert', 'experienced', 'principal']
    juniority = ['junior', 'jr.', 'jr', 'intern']
    for i in seniority:
        if i in title:
            return 'senior'
    for i in juniority:
        if i in title:
            return 'junior'
    else:
        return 'unspecified''')

    st.code('''df['Seniority'] = df['Job Title'].apply(seniority)
df.sample(3) # Sample 3 random postings''')

    def seniority(title):
        '''Identify and group specific job titles'''

        title = title.lower().strip()

        seniority = [
            'senior', 'sr.', 'sr', 'lead', 'expert', 'experienced', 'principal'
        ]
        juniority = ['junior', 'jr.', 'jr', 'intern']

        for i in seniority:
            if i in title:
                return 'senior'

        for i in juniority:
            if i in title:
                return 'junior'

        else:
            return 'unspecified'

    df['Seniority'] = df['Job Title'].apply(seniority)
    st.markdown(
        'Now we have a new column, *Seniority*, which specifies the precedence of each posting.'
    )
    st.dataframe(df.sample(3))
    st.code('df.Seniority.value_counts()')
    st.code(df.Seniority.value_counts())
    titles = pd.DataFrame({
        'Position': ['Unspecified', 'Senior', 'Junior'],
        'Total': [595, 325, 60]
    })
    st.markdown('**Bar chart of Seniority**')
    st.altair_chart(
        alt.Chart(titles).mark_bar().encode(y='Position', x='Total'))
    st.markdown(
        '''This bar chart shows the distribution of seniority in the job title listings. 
    While the majority of titles do not specify seniority, it seems to make intuitive sense that there 
    is a greater demand for experienced software engineers as opposed to junior or new grad positions. 
    The lack of junior positions could also be explained by the notion that most of those listings would be 
    offered as internships rather than full time postions -and thus wouldn't be listed on a job-hunting 
    website such as Glassdoor.''')

    st.subheader('Parsing Salary Estimates')
    st.markdown(
        'Next I separated the Glassdoor Salary Estimates into lows and highs to get an average.'
    )
    st.code('''df.get('Salary Estimate').unique()''')
    st.text(df.get('Salary Estimate').unique())
    st.code('''def salary_simplified(salary):
    salary_simp = salary.split('(')[0].replace('K','').replace('$','')
    minimum = int(salary_simp.split('-')[0])
    maximum = int(salary_simp.split('-')[1])
    return minimum, maximum''')
    st.code('''salary_ranges = df['Salary Estimate'].apply(salary_simplified)
    ''')

    def salary_simplified(salary):
        salary_simp = salary.split('(')[0].replace('K', '').replace('$', '')
        minimum = int(salary_simp.split('-')[0])
        maximum = int(salary_simp.split('-')[1])
        return minimum, maximum

    salary_ranges = df['Salary Estimate'].apply(salary_simplified)

    st.subheader('Reverse Geocoding Locations')
    st.markdown(
        '''In order to visualize the locations of the job postings in the data frame, 
        I needed a way to plot each posting on a map. However, the data did not come 
        with any geographic information about the locations of the postings. To solve 
        this problem I used Google Maps Cloud API to reverse geocode each city's location 
        and obtain it's lattitude and longitude coordinates. The following code cell assigns 
        each job's Location listing with the corresponding geographic coordinates.'''
    )
    st.code('''df['LAT'] = None
df['LON'] = None

for i in range(len(df.Location)):
    geocode_result = gmaps_key.geocode(df.Location.iloc[i])
    try:
        lat = geocode_result[0]['geometry']['location']['lat']
        lon = geocode_result[0]['geometry']['location']['lng']
        df.loc[i, 'LAT'] = lat
        df.loc[i, 'LON'] = lon
    except:
        lat = None
        lng = None''')

    st.markdown(
        '''The next code block simplifies the geocoding by creating a new data frame that stores 
    geographic coordinates, cities, and the number of times they appear in the original table.'''
    )

    st.code('''city_counts = df.groupby('Location').count().get('Job Title')
df_group = pd.DataFrame()
df_group['Lat'] = df['LAT']
df_group['Lon'] = df['LON']
df_group['City'] = df['Location']

cities = pd.DataFrame()
cities['Count'] = city_counts
cities = cities.reset_index()

df_geo = df_group.merge(cities, left_on='City', right_on='Location')
df_geo = df_geo.drop_duplicates(['City'], keep='first').drop(['City'], axis=1)
    ''')

    bubble_map = folium.Map(location=[37, -102], zoom_start=4)
    st.markdown(
        '''The map will default it's location over the United States.''')
    st.code('bubble_map = folium.Map(location=[37, -102], zoom_start=4)')

    df_geo = pd.read_csv('df_geo.csv')
    for i in range(len(df_geo)):
        folium.Circle(location=[df_geo.Lat.iloc[i], df_geo.Lon.iloc[i]],
                      popup=df_geo.Location.iloc[i],
                      radius=int(df_geo.Count.iloc[i]) * 10000,
                      color='#7551f8',
                      fill=True,
                      fill_color='#7551f8').add_to(bubble_map)

    st.code('''for i in range(len(df_geo)):
    folium.Circle(location=[df_geo.Lat.iloc[i], df_geo.Lon.iloc[i]],
            popup=df_geo.Location.iloc[i],
            radius=int(df_geo.Count.iloc[i]) * 10000,
            color='#7551f8',
            fill=True,
            fill_color='#7551f8').add_to(bubble_map)''')

    st.markdown('**Bubble Map of Jobs based on Posting Density**')
    st.markdown(bubble_map._repr_html_(),
                unsafe_allow_html=True)  # Allows Folium map to be displayed
    st.markdown('')
    st.markdown(
        '''This Bubble Map of the United States plots each job listing's location 
    where the radius of the bubble is a factor corresponding to the number of postings at 
    each location. From the map we can see that there are a large number of postings in 
    Salt Lake City, Chicago, Burlington, New York, San Jose, and Seattle. The concentration 
    of multiple circles in the Bay Area and East coast reflect a high volume of postings and 
    signify these areas as "Tech Hubs."''')

    st.info(
        ''' by: [Daman Heer](https://damehero.github.io/) | source: [GitHub](https://github.com/damehero/StreamlitApp) '''
    )

    st.markdown("<h1 style='text-align: center; color: red;'>Thank you!</h1>",
                unsafe_allow_html=True)
    st.latex('a^2 + b^2 = c^2')
