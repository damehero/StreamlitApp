import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import joblib




def write():
    st.title('Glassdoor Salary Predictor')
    st.header('Predict a potential salary')
    st.markdown('''Uses Sci-Kit Learn Random Forest Regressor based on the following specifiable traits:''')

    option = st.selectbox(
        'Select Job Type',
        ('Software Engineering', 'Data Science', 'Product Design'))

    if option == 'Software Engineering':

        df = pd.read_csv('swe_cleaned.csv')
        swe_model = joblib.load('model.pkl')

        st.subheader('Company Details: \n Check Glassdoor for exact values, if unsure')

        rating = st.slider('Glassdoor Rating of the Company',
                        min_value=0.0,
                        max_value=5.0,
                        step=0.1)
        age = st.number_input('Age of the Company', step=1.0, min_value=0.0)

        st.subheader('Details about the Job:')

        jobhq = st.radio("Is the Job at Headquarters? (0 for No, 1 for Yes)",
                        options=[0, 1])
        job_type_num = st.selectbox("Job Type", options=df["job_simp"].unique())


        def title_number_simplifier(title):
            if 'reg' in title.lower():
                return 1
            elif 'back-end' in title.lower():
                return 2
            elif 'full-stack' in title.lower():
                return 3
            elif 'web' in title.lower():
                return 4
            elif 'data' in title.lower():
                return 5
            elif 'mobile' in title.lower():
                return 6
            elif 'systems' in title.lower():
                return 7


        job_type_num1 = title_number_simplifier(job_type_num)


        def seniority_number(title):
            if 'senior' in title.lower():
                return '1'
            elif 'junior' in title.lower():
                return '2'
            else:
                return '3'


        seniority_num = st.radio("Senior role?", options=["Senior", "Not Senior"])
        seniority_num1 = seniority_number(seniority_num)
        seniority_num2 = seniority_number(seniority_num)
        seniority_num3 = seniority_number(seniority_num)


        st.subheader('Your skills:')
        python_yn = st.radio("Python (0 for No, 1 for Yes)", options=[0, 1])
        java_yn = st.radio("Java (0 for No, 1 for Yes)", options=[0, 1])
        javascript_yn = st.radio("Javascript (0 for No, 1 for Yes)", options=[0, 1])
        c_yn = st.radio("C (0 for No, 1 for Yes)", options=[0, 1])
        html_yn = st.radio("HTML/CSS (0 for No, 1 for Yes)", options=[0, 1])

        features = [
            rating, jobhq, age, python_yn, java_yn, javascript_yn, c_yn, html_yn,
            job_type_num1, seniority_num1, seniority_num2, seniority_num3
        ]
        final_features = np.array(features).reshape(1, -1)

        if st.button('Predict'):
            prediction = swe_model.predict(final_features)
            st.balloons()
            st.success(f'Your predicted salary is US$ {round(prediction[0],3)*1000} ')


    elif option == 'Data Science':

        df = pd.read_csv('data_cleaned.csv')

        data_model = joblib.load('data_model.pkl')

        st.subheader('Company Details: \n Check Glassdoor for exact values, if unsure')

        rating = st.slider('Glassdoor Rating of the Company',
                        min_value=0.0,
                        max_value=5.0,
                        step=0.1)
        age = st.number_input('Age of the Company', step=1.0, min_value=0.0)

        st.subheader('Details about the Job:')

        jobhq = st.radio("Is the Job at Headquarters? (0 for No, 1 for Yes)",
                        options=[0, 1])
        job_type_num = st.selectbox("Job Type", options=['Data Scientist', 'Data Engineer', 'Analyst', 'Director', 'Manager', 'Machine Learning Engineer', 'Research', 'Software'])


        def number_simplifier(title):
            if "data scientist" in title.lower():
                return 3
            elif "data engineer" in title.lower():
                return 2
            elif "analyst" in title.lower():
                return 1
            elif "director" in title.lower():
                return 4
            elif "manager" in title.lower():
                return 5
            elif "machine learning engineer" in title.lower():
                return 6
            elif "unspecified" in title.lower():
                return 7
            elif "research" in title.lower():
                return 8
            elif "software" in title.lower():
                return 9

        job_type_num1 = number_simplifier(job_type_num)

        def senior_simplifier(title):
            if title == "Senior":
                return 1
            else:
                return 2


        seniority_num = st.radio("Senior role?", options=["Senior", "Not Senior"])
        seniority_num1 = senior_simplifier(seniority_num)


        st.subheader('Your skills:')
        python_yn = st.radio("Python (0 for No, 1 for Yes)", options=[0, 1])
        R_yn = st.radio("R (0 for No, 1 for Yes)", options=[0, 1])
        aws = st.radio("AWS (0 for No, 1 for Yes)", options=[0, 1])
        spark = st.radio("Spark (0 for No, 1 for Yes)", options=[0, 1])
        excel = st.radio("Excel (0 for No, 1 for Yes)", options=[0, 1])

        features = [
            rating, jobhq, age, python_yn, R_yn, aws, spark, excel,
            job_type_num1, seniority_num1
        ]
        final_features = np.array(features).reshape(1, -1)

        if st.button('Predict'):
            prediction = data_model.predict(final_features)
            st.balloons()
            st.success(f'Your predicted salary is US$ {round(prediction[0],3)*1000} ')


    elif option == 'Product Design':

        df = pd.read_csv('dsgn_cleaned.csv')

        dsgn_model = joblib.load('dsgn_model.pkl')

        st.subheader(
            'Company Details: \n Check Glassdoor for exact values, if unsure')

        rating = st.slider('Glassdoor Rating of the Company',
                           min_value=0.0,
                           max_value=5.0,
                           step=0.1)
        age = st.number_input('Age of the Company', step=1.0, min_value=0.0)

        st.subheader('Details about the Job:')

        jobhq = st.radio("Is the Job at Headquarters? (0 for No, 1 for Yes)",
                         options=[0, 1])
        job_type_num = st.selectbox("Job Type",
                                    options=[
                                        'Product Designer', 'UI/UX Designer',
                                        'Graphic Designer', 'Structural Designer', 'Web Designer',
                                        'Unspecified'
                                    ])

        def number_simplifier(title):
            if "product designer" in title.lower():
                return 6
            elif "ui/ux designer" in title.lower():
                return 5
            elif "graphic designer" in title.lower():
                return 2
            elif "structural designer" in title.lower():
                return 3
            elif "web designer" in title.lower():
                return 4
            elif "unspecified" in title.lower():
                return 1

        job_type_num1 = number_simplifier(job_type_num)

        def senior_simplifier(title):
            if title == "Senior":
                return 1
            else:
                return 2

        seniority_num = st.radio("Senior role?",
                                 options=["Senior", "Not Senior"])
        seniority_num1 = senior_simplifier(seniority_num)

        st.subheader('Your skills:')
        figma_yn = st.radio("Figma (0 for No, 1 for Yes)", options=[0, 1])
        adobe_yn = st.radio("Adobe Creative Suite (0 for No, 1 for Yes)", options=[0, 1])
        cad_yn = st.radio("CAD Software (0 for No, 1 for Yes)", options=[0, 1])
        html_css_js_yn = st.radio("HTML/CSS/JavaScript (0 for No, 1 for Yes)", options=[0, 1])
        photo_yn = st.radio("Photography (0 for No, 1 for Yes)", options=[0, 1])
        graphic_yn = st.radio("Graphics (0 for No, 1 for Yes)", options=[0, 1])

        features = [
            rating, jobhq, age, figma_yn, adobe_yn, cad_yn, html_css_js_yn,
            photo_yn, graphic_yn, job_type_num1, seniority_num1
        ]
        final_features = np.array(features).reshape(1, -1)

        if st.button('Predict'):
            prediction = dsgn_model.predict(final_features)
            st.balloons()
            st.success(
                f'Your predicted salary is US$ {round(prediction[0],3)*1000} ')
