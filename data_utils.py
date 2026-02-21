import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    # Reads the CSV file created by generate_data.py
    df = pd.read_csv("data/global_retail_sales.csv")
    
    # Ensures that time columns are recognized as date objects
    df['order_date'] = pd.to_datetime(df['order_date'])
    
    return df