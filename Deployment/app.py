import streamlit as st
import pandas as pd
import numpy as np
import joblib
import eda
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.header('Credit Card Default Prediction')
st.write("""
Created by Ahmad Dani Rifai

Use the sidebar to select input features.
""")

@st.cache
def fetch_data():
    df = pd.read_csv('P1G5_Set_1_Ahmad_Dani.csv')
    return df

df = fetch_data()
st.write(df)

st.sidebar.header('User Input Features')

def user_input():
    gender = st.sidebar.radio('Gender', ['Male', 'Female'])
    limit_balance = st.sidebar.slider('Limit Balance', 0, 300000, 150000)
    education_level = st.sidebar.selectbox('Education Level', ['Graduate School', 'University', 'High School', 'Others'])
    marital_status = st.sidebar.selectbox('Marital Status', ['Married', 'Single', 'Others'])
    age = st.sidebar.slider('Age', 20, 60, 30)
    pay_0 = st.sidebar.selectbox('Payment Status (Month 1)', ['Paid in full', 'Revolve', 'Delay', 'Default'])
    bill_amt_1 = st.sidebar.number_input('Bill Amount (Month 1)', min_value=0, value=75000)
    pay_amt_1 = st.sidebar.number_input('Payment Amount (Month 1)', min_value=0, value=75000)

    # Mapping categorical input to numerical values
    sex_map = {'Male': 0, 'Female': 1}
    education_map = {'Graduate School': 1, 'University': 2, 'High School': 3, 'Others': 4}
    marital_map = {'Married': 0, 'Single': 1, 'Others': 2}
    pay_map = {'Paid in full': 0, 'Revolve': 1, 'Delay': 2, 'Default': 3}

    # Convert user input to numerical values
    gender = sex_map[gender]
    education_level = education_map[education_level]
    marital_status = marital_map[marital_status]
    pay_0 = pay_map[pay_0]

    data = {
        'limit_balance': limit_balance,
        'sex': gender,
        'education_level': education_level,
        'marital_status': marital_status,
        'age': age,
        'pay_0': pay_0,
        'bill_amt_1': bill_amt_1,
        'pay_amt_1': pay_amt_1
    }
    features = pd.DataFrame(data, index=[0])
    return features


input = user_input()

#  Display user input data
st.subheader('User Input')
st.write(input)

# Load model
load_model = joblib.load("model.pkl")

# Predict based on user input
prediction = load_model.predict(input)

# Display prediction result
st.subheader('Prediction')
prediction = load_model.predict(input)

if prediction == 1:
    prediction_text = 'Default Payment: Yes'
else:
    prediction_text = 'Default Payment: No'

st.subheader('Prediction')
st.write(prediction_text)
# if prediction == 1:
#     prediction = 'Placed'
# else:
#     prediction = 'Not Placed'

# st.write('Based on user input, the placement model predicted: ')
# st.write(prediction)