# StreamlitApp: STEM Career Project

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

* Created a [web application](https://stem-career-project.herokuapp.com/) to serve as an interactive and visual expansion on an assignment originally submitted as a final prjoect for COGS 108: Data Science in Practice, taught remotely by UC San Diego in Spring 2020.
* Webscraped over 1000 unique job postings from [Glassdoor.com](https://www.glassdoor.com/sitedirectory/title-jobs.htm) using Selenium and Chromedriver
* Feature engineered from the text of each job description to quantify the value companies place on skills such as Python, Java, AWS, Figma and many other skills.
* Optimized a Random Forest Regressor from scikit-learn to create a tool that estimates software engineering, data science, and product design salaries (MAE ~ $7K)
* Built a web application for users to input data and receive an estimate, using Streamlit and Heroku.
 

## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, altair, selenium, streamlit, pickle  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium  
**Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905  

## Web Scraping
Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:
*	Job title
*	Salary Estimate
*	Job Description
*	Rating
*	Company 
*	Location
*	Company Headquarters 
*	Company Size
*	Company Founded Date
*	Type of Ownership 
*	Industry
*	Sector
*	Revenue
*	Competitors 

## Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for the model. I made the following changes and created the following variables:

*	Parsed numeric data out of salary 
*	Removed rows without salary 
*	Parsed rating out of company text 
*	Made a new column for company city and state 
*	Added a column for if the job was at the company’s headquarters 
*	Transformed founded date into age of company 
*	Made columns for if different skills were listed in the job description:
    * Python  
    * Java  
    * R  
    * AWS  
    * Excel 
*	Column for simplified job title and Seniority 

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 

![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/salary_by_job_title.PNG "Salary by Position")
![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/positions_by_state.png "Job Opportunities by State")
![alt text](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/correlation_visual.png "Correlations")

## Model Building & Performance

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.   

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

I tried three different models:
*	**Multiple Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
*	**Random Forest** – Again, with the sparsity associated with the data, I thought that this would be a good fit. 

The Random Forest model was the best suited approach for the test and validation sets. 
*	**Random Forest** : MAE = 7.41

## Productionization 
In this step, I built a Streamlit web app to display the notebook with data visualizations, the salary predictor, and the results of the project.


