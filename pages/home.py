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
    st.markdown('''• How much will my **salary** be worth with **living cost** factored in?'''
    )

    st.header('Background & Prior Research')
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
        In fact, most unicorn companies (privately-held startups valued at over $1 billion) all originate from the Silicon Valley. Why are so many entrepreneurs and technologists drawn to settle here?
        Why did leading companies such as Google, Apple, Facebook all start in Silicon Valley? Were those companies suplemented by college students who went to large and proximal research universities
        (i.e. Stanford and UC Berkeley)?</p> 
        <p style='text-align: justify; '>We wanted to find out if any of these factors actually contributed to the success and image of Silicon Valley and how might gain insight as to where the next 
        Silicon Valley may come from. From <a href="https://builtin.com/tech-hubs">Builtin.com</a> we learned that San Francisco only has 4,346 tech companies and is the third most expensive city in the U.S. to live in, while New York City has 5,196 tech companies 
        and is the second most expensive city to live in. Garnering examples like these spark insight and test our assumptions about these locations.</p>''',
                unsafe_allow_html=True)

    st.header('Hypothesis')
    st.markdown(
        '''<p style='text-align: justify; '>We predict that we are going to observe a <b>positive correlation</b> between certain states and salaries <b>based on our selected majors</b>, and that there are <b>optimal regions</b> that will increase the likelihood of earning a higher salary based on career/college major.</p>''',
        unsafe_allow_html=True)

    st.header('Data')
    st.markdown(''' 
        <p style='text-align: justify; '>An ideal dataset would cover all the discrepancies we’re seeking to address with these research questions. Since our question is about the city mostly, we need geographic-specific 
        data that will tell us the average pay in a city for a given career and the ability to address the fact that living costs heavily factor into the true value of the salary in any given place since the living costs can 
        shift drastically from city to city. Additionally this data would have to be collected on a national level and consistent regardless of location. In order to do this, we have to find a national provider of data that rates 
        all cities by the same metric such as a tourism or housing service. Also data about the average pay of a career nationally would help us place greater weight on whether the salary increase is worth it regardless of the living 
        costs. Since we are looking at several different majors which have to be treated independently, we will need a great number of observations for each given major/career path with little overlap allowed for similar fields that 
        connotes similar pay (i.e. anything careers in similar sectors Graphic Designer or UI designer). To summarize, the data we collect should be able to be matched by city or state, while allowing us to make a correlation between 
        the growth rate of certain areas to the relationship between geo-specific salary and living costs in order to establish a ranking system of best places to go with a given major/career path.</p>''',
        unsafe_allow_html=True)

    st.header('Ethics & Privacy')
    st.markdown(''' 
        <p style='text-align: justify; '>As with any form of data investigation, certain precautions and best-practice procedures must be followed in order to adhere to ethical and privacy standards. By using datasets that have been 
        generated by reputable sources (US Census Bureau, Department of Labor & Commerce, WSJ) we have ensured to the best of our ability that the data being used in our project was collected in an equitable and consensual manner. 
        The datasets we have chosen are public and free to use on our project, and don't seem to interfere with our purposes.</p>''',
        unsafe_allow_html=True)
    st.markdown(''' 
        <p style='text-align: justify; '>Additionally, because we are drawing from such a general and broad range of anonymous statistics, we can naturally avoid violating the privacy of any particular individual. However, there are still 
        certain ethical issues that we must be wary of as we complete our project. A key issue that can arise in our particular project has to do with the biases that already exist in our data. For example, certain datasets may be incomplete 
        or weigh heavily in favor of one category due to convenience sampling. It is our responsibility as data scientists to identify these discrepancies and try to mitigate their impact on our predictions by cross-referencing additional data 
        sources. Something that we must also be conscious of is that we are excluding other universities across the globe, mainly because we want to be specific with our data analyses. Currently, we are only focusing on individuals who have pursued 
        Bachelor degrees, which excludes those who did not get a traditional 4-year degree. This could lead to some biases in our data, but we hope to account for that by narrowing down the population we are examining.</p>''',
        unsafe_allow_html=True)
