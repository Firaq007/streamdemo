import streamlit as st
import pandas as pd
import numpy as np

# Function to calculate investment growth
def calculate_investment(principal, rate, time):
    return principal * (1 + rate) ** time

# Streamlit app header
st.title('Investment Calculator')

# Sidebar for user input
st.sidebar.header('Input Parameters')
principal = st.sidebar.number_input('Enter Principal Amount:', min_value=0.0)
rate = st.sidebar.number_input('Enter Annual Interest Rate:', min_value=0.0)
time = st.sidebar.number_input('Enter Time Period (in years):', min_value=0)

# Calculate investment growth
if st.sidebar.button('Calculate'):
    result = calculate_investment(principal, rate, time)
    st.write(f'Principal Investment: ${principal}')
    st.write(f'Annual Interest Rate: {rate}%')
    st.write(f'Time Period: {time} years')
    st.write(f'Future Value: ${result:.2f}')
    st.write(f'Try Jewlery that you can buy with this Investement: https://microchippayments.com/demo/')
