import pandas as pd
import sqlite3
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer


def load_data_from_db(db_file_path, table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file_path)

    # Load data from the specified table
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

    # Close the database connection
    conn.close()

    return df


# Load cleaned data from the database
df_from_db = load_data_from_db('cleaned_data.db', 'cleaned_transaction_data')

# Create a Pygwalker dashboard with Streamlit
st.title("Transaction Data Dashboard")

# Display the dataframe
st.write(df_from_db)

# Create a Pygwalker dashboard
StreamlitRenderer(df_from_db).explorer()
