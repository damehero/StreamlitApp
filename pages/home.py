import streamlit as st


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

    st.header('Research Questions')
    st.markdown('''• Where is the 'best' place to live based on my **major** and **career path**?''' )
    st.markdown('''• What are the most popular **industries & sectors** for the roles that I'm seeking?''')
    st.markdown('''• How much will my **adjusted salary** be worth with **living cost** factored in?'''
    )

    st.header('Background & Prior Work')
    st.markdown(
        '''<p style='text-align: justify; '>As college students on track to graduation, we wanted to understand whether or not acquiring a job with a high salary would require one to relocate to a different state. 
        Although we currently know that there are certain regions that are known to be ideal for various career paths (i.e. Silicon Valley for majors related to technology), 
        we wanted to an in-depth analysis about lesser-known locations that may ideal for STEM majors.</p> 
        <p style='text-align: justify; '>As Cognitive Science students looking to work in tech, we were namely curious about roles in <b>Software Engineering</b>, <b>Data Science</b>, and <b>Product Design</b>.</p> 
        <p style='text-align: justify; '>After doing some research on other projects and articles that analyzed the correlation 
        between salaries and the value of having a college degree, we decided to do an investigation on salaries and their variation in different geographical locations. Companies have made general calculators (i.e. <a href="https://www.payscale.com/">PayScale.com</a>), 
        which make salary estimates based on factors such as the alma matter or university degree, but we wanted to go the extra mile 
        and further investigate the cost of living in certain regions and how it may pay off.</p>''',
        unsafe_allow_html=True)
    st.markdown(''' 
        <p style='text-align: justify; '>The formulation of our research questions led us into the discussion of where the next Tech Hub might emerge from. As we know today, Silicon Valley is widely considered to be the main center for innovation and tech startups. 
        In fact, most unicorn companies (privately-held startups valued at over $1 billion) all originate from the Silicon Valley. So we wondered, where are the next best places in the US with an abundance of optimal job opportunities in technology?</p> 
        <p style='text-align: justify; '>We wanted to find out if Silicon Valley is successful because people found that their average salary (with living costs factored in) still leaves sufficient leftover money to spend on non-essential “nice-to-have” costs. From <a href="https://builtin.com/tech-hubs">Builtin.com</a> we learned that San Francisco only has 4,346 tech companies and is the third most expensive city in the U.S. to live in, while New York City has 5,196 tech companies 
        and is the second most expensive city to live in. Garnering examples like these spark insight and test our assumptions about these locations.</p>''',
                unsafe_allow_html=True)

    st.header('Hypothesis')
    st.markdown(
        '''<p style='text-align: justify; '>We predict that we are going to observe a <b>positive correlation</b> between certain states and salaries <b>based on our selected majors</b>, and that there are <b>optimal regions</b> that will increase the likelihood of earning a higher salary based on career/college major.</p>''',
        unsafe_allow_html=True)

    st.header('Data')
    st.markdown('''
    <p style='text-align: justify; '> An ideal dataset would cover all the specifics we’re seeking to address in our research questions. Since our questions are mostly geo-centric, we will need geographic-specific data 
    that can tell us about the average pay in a city for a given career as well as a label with living costs in that area.
    Additionally, this data would have to be collected on a national level and be consistent regardless of location. In order to do this, we need to find a national provider of data that rates 
    all cities by the same metric such as a tourism or housing service. Also data about the average pay of a career nationally would help us place greater weight on whether the salary increase is worth it regardless of 
    the living costs. Since we are looking at several different majors which have to be treated independently, we will need a great number of observations for each given major/career path with little overlap allowed for 
    similar fields that connotes similar pay (i.e. anything careers in similar sectors Graphic Designer or UI designer). To summarize, the data we collect should be able to be matched by city or state, while allowing us to 
    make a correlation between the growth rate of certain areas to the relationship between geo-specific salary and living costs in order to establish a ranking system of best places to go with a given major/career path.</p>''',
                unsafe_allow_html=True)
    st.markdown(''' 
        1. Software Engineering, Data Science, and Product Design job postings in the US on [GlassDoor.com](https://www.glassdoor.com/index.htm)''')
    st.markdown('''
        2. Cost of Living Index from [BestPlaces.com](https://www.bestplaces.net/cost-of-living/)''')

