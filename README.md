# Transaction Data Pipeline

This repository contains a transaction data pipeline that generates, cleans, and visualizes transaction data.

## Features

1. **Data Generation**
    - `create_dirty_data.py`: Generates synthetic, messy transaction data and stores it in a CSV file.

2. **Data Cleaning**
    - `clean_and_create_db.py`: Cleans the generated data and stores it in an SQLite database.

3. **Data Visualization**
    - `app.py`: Loads cleaned data from the database and visualizes it using Streamlit and Pygwalker.
