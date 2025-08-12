import streamlit as st
import psycopg2
import pandas as pd

# Streamlit app title
st.title("PostgreSQL Connection with Streamlit")

# DB connection details
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "abi"
DB_USER = "postgres"
DB_PASS = "birmingham"

# Connect to PostgreSQL
def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

# Fetch data
def fetch_data():
    conn = get_connection()
    query = "SELECT * FROM movies;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

if st.button("Load Data"):
    try:
        data = fetch_data()
        st.write(data)
    except Exception as e:
        st.error(f"Error: {e}")
