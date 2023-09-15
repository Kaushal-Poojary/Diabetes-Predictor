
# Diabetes Predictor

## Overview

This is a diabetes predictor application that predicts the likelihood of a person having diabetes based on various health parameters. The application utilizes several machine learning models, including logistic regression, k-nearest neighbors (KNN), random forest classifier, support vector classifier (SVC), Gaussian naive Bayes, and decision tree, to make predictions. After thorough evaluation, the support vector classifier (SVC) achieved the highest accuracy and was chosen as the final model for deployment.

## Motive

The primary goal of this project is to create a user-friendly tool that can help individuals assess their risk of diabetes using a set of common health parameters. Early detection and prevention of diabetes are essential for improving public health, and this application aims to contribute to that goal by providing a convenient and accessible means of risk assessment.

## Models Used

1. **Logistic Regression** (Accuracy: 75.97%)
   
   Logistic regression is a simple yet effective classification algorithm that models the probability of a binary outcome.

3. **K-Nearest Neighbors (KNN)** (Accuracy: 73.37%)
   
   KNN is a non-parametric and instance-based learning algorithm that classifies data points based on the majority class of their k-nearest neighbors.

5. **Random Forest Classifier** (Accuracy: 74%)
   
   Random forests are an ensemble learning method that combines multiple decision trees to improve classification accuracy and reduce overfitting.

7. **Support Vector Classifier (SVC)** (Accuracy: 78.57%)
   
   SVC is a powerful classification algorithm that finds the hyperplane that best separates data points into different classes while maximizing the margin between the classes.

9. **Gaussian Naive Bayes** (Accuracy: 76.62%)
    
   Gaussian Naive Bayes is a probabilistic classification algorithm based on Bayes' theorem, assuming that the features are normally distributed.

11. **Decision Tree** (Accuracy: 74%)
    
    Decision trees are a popular classification algorithm that recursively partitions the data into subsets based on the most significant attribute.

## Features

The diabetes predictor takes the following input parameters into account:

- **Blood Pressure:** The systolic blood pressure in mm Hg.
- **Skin Thickness:** The thickness of the skinfold at the triceps in mm.
- **Insulin:** The level of insulin measured in milli-international units per milliliter (mu U/ml). 
- **Glucose:** The concentration of glucose in the blood, typically measured in milligrams per deciliter (mg/dL).
- **BMI (Body Mass Index):** The Body Mass Index, calculated as weight (kg) / (height (m))^2.
- **Diabetes Pedigree Function:** A function that scores the family history of diabetes.
- **Age:** The age of the individual.
- **Pregnancies:** The number of times the person has been pregnant.

## Data Cleaning and Feature Engineering

Before training the machine learning models, the dataset underwent data cleaning and feature engineering to ensure the quality of the data and enhance predictive performance. This process involved handling missing values, scaling features, and creating relevant new features from the existing ones.

## Data Reduction

To reduce the dimensionality of the dataset and improve model efficiency, feature selection techniques were applied to identify the most important predictors.

## Frontend Using Streamlit

The frontend of this diabetes predictor application was developed using Streamlit, a user-friendly Python library for building web applications. Streamlit provides an interactive and responsive interface for users to input their health parameters and receive predictions.

## Hosting Using Render

The application is hosted using Render, a cloud platform that simplifies the deployment and hosting of web applications. Render provides a reliable and scalable infrastructure for running web-based machine learning applications.

## Conclusion

After evaluating multiple machine learning models, the support vector classifier (SVC) demonstrated the highest accuracy and was chosen as the final model for deployment. This diabetes predictor serves as a valuable tool for individuals to assess their risk of diabetes based on common health parameters, contributing to early detection and prevention efforts.

## Links

1. [COVID-19 Dataset on Kaggle](https://www.kaggle.com/datasets/meirnizri/covid19-dataset)

2. [Diabetes Predictor Web Application](https://diabetes-predictor-khun.onrender.com/#diabetes-prediction)
