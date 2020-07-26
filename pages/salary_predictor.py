import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import joblib


df = pd.read_csv('swe_cleaned.csv')
model = joblib.load('model.pkl')


def write():
    st.title('Glassdoor Salary Predictor')
    st.header('Predict the potential salary')
    st.markdown('''Uses a Random Forest Regressor from Sci-Kit Learn.''')

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
        prediction = model.predict(final_features)
        st.balloons()
        st.success(f'Your predicted salary is US$ {round(prediction[0],3)*1000} ')