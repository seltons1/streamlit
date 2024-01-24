import streamlit as st
import requests
import pandas as pd
import plotly.express as px


def format_number(value,  prefix = '' ):
    '''Format decimal values'''

    for und in ['','m']:
        if value < 1000:
            return f'{prefix} {value:.2f} {und}'
        value /= 1000
    return f'{prefix} {value:.2f} mi'

# Set dashboard title
st.title('Dashboard Example')

# Get data from API
url = 'https://labdados.com/produtos'
response = requests.get(url)
data = pd.DataFrame.from_dict(response.json())

# Create columns to show metrics
col1, col2 = st.columns(2)
col1.metric('Total', format_number(data['Preço'].sum(), 'R$'))
col2.metric('Quant', format_number(data.shape[0]))

# Show table with data
st.dataframe(data)


