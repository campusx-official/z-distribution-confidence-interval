import streamlit as st
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

st.set_page_config(page_title='Confidence Interval Calculator', layout='wide')

st.title('Confidence Interval Calculator for Z Procedure')

st.write('''
This app calculates the confidence interval for a population mean using a Z-procedure and displays a graph of the interval.
''')

with st.sidebar:
    st.header('Input Parameters')
    confidence_level = st.slider('Confidence Level (%)', 0, 100, 95, 1)
    sample_mean = st.number_input('Sample Mean', value=0.0)
    population_std_dev = st.number_input('Population Standard Deviation', value=1.0)
    sample_size = st.number_input('Sample Size', value=30, min_value=1, step=1)

# Calculate the critical value (z-score) and margin of error
z_score = norm.ppf(1 - (1 - confidence_level / 100) / 2)
margin_of_error = z_score * (population_std_dev / np.sqrt(sample_size))

# Calculate the confidence interval
lower_limit = sample_mean - margin_of_error
upper_limit = sample_mean + margin_of_error

# Display results
st.write(f'Critical Value (z-score): {z_score:.2f}')
st.write(f'Margin of Error: {margin_of_error:.2f}')
st.write(f'Confidence Interval: ({lower_limit:.2f}, {upper_limit:.2f})')

# Plot the confidence interval
fig, ax = plt.subplots(figsize=(3, 2))

ax.bar(['Lower Limit', 'Upper Limit'], [lower_limit, upper_limit], color='lightblue')
ax.plot(['Lower Limit', 'Upper Limit'], [lower_limit, upper_limit], color='red', linewidth=2)
ax.axhline(sample_mean, color='green', linestyle='--', label='Sample Mean')

ax.set_ylabel('Value')
ax.set_title('Confidence Interval')
ax.legend()

st.pyplot(fig)
