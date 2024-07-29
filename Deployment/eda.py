import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.header('Exploratory Data Analysis')
st.write("""
Created by Ahmad Dani Rifai

""")
@st.cache
def fetch_data():
    df = pd.read_csv('P1G5_Set_1_Ahmad_Dani.csv')
    return df

df = fetch_data()
st.write(df)

# Rata-rata Payment Next Month berdasarkan Age
average_price_by_age = df.groupby('age')['default_payment_next_month'].mean().sort_values().reset_index()
average_price_by_age.columns = ['Age', 'Rata-rata Payment Next Month']

# Plot menggunakan plotly untuk interaktivitas yang lebih baik
st.subheader('Rata-rata Payment Next Month berdasarkan Age')
fig = px.bar(average_price_by_age, x='Age', y='Rata-rata Payment Next Month', 
             title='Rata-rata Payment Next Month berdasarkan Age', 
             labels={'Rata-rata Payment Next Month': 'Rata-rata Payment Next Month', 'Age': 'Age'})
st.plotly_chart(fig)

# Rata-rata Payment Next Month berdasarkan Education Level
average_price_by_education = df.groupby('education_level')['default_payment_next_month'].mean().sort_values().reset_index()
average_price_by_education.columns = ['Education Level', 'Rata-rata Payment Next Month']

# Plot menggunakan plotly
st.subheader('Rata-rata Payment Next Month Berdasarkan Education Level')
fig = px.bar(average_price_by_education, x='Education Level', y='Rata-rata Payment Next Month', 
             title='Rata-rata Payment Next Month Berdasarkan Education Level', 
             labels={'Rata-rata Payment Next Month': 'Rata-rata Payment Next Month', 'Education Level': 'Education Level'})
st.plotly_chart(fig)

# Rata-rata Payment Next Month berdasarkan Marital Status
average_price_by_marital_status = df.groupby('marital_status')['default_payment_next_month'].mean().sort_values().reset_index()
average_price_by_marital_status.columns = ['Marital Status', 'Rata-rata Payment Next Month']

# Plot menggunakan plotly
st.subheader('Rata-rata Payment Next Month Berdasarkan Marital Status')
fig = px.bar(average_price_by_marital_status, x='Marital Status', y='Rata-rata Payment Next Month', 
             title='Rata-rata Payment Next Month Berdasarkan Marital Status', 
             labels={'Rata-rata Payment Next Month': 'Rata-rata Payment Next Month', 'Marital Status': 'Marital Status'})
st.plotly_chart(fig)

# Rata-rata Payment Next Month berdasarkan Pay_0
average_price_by_pay_0 = df.groupby('pay_0')['default_payment_next_month'].mean().sort_values().reset_index()
average_price_by_pay_0.columns = ['Pay_0', 'Rata-rata Payment Next Month']
