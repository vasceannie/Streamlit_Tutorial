import pandas as pd
import numpy as np


def clean_messy_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path, sep=",")

    # Clean TransactionID
    df['TransactionID'] = df['TransactionID'].fillna('UNKNOWN')

    # Clean TransactionDate
    df['TransactionDate'] = pd.to_datetime(df['TransactionDate'], errors='coerce')
    df['TransactionDate'] = df['TransactionDate'].fillna(pd.Timestamp('1970-01-01'))

    # Clean Amount
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df['Amount'] = df['Amount'].fillna(0.0)

    # Clean Currency
    valid_currencies = ['USD', 'EUR', 'JPY', 'GBP', 'AUD']
    df['Currency'] = df['Currency'].apply(lambda x: x if x in valid_currencies else 'UNKNOWN')

    # Clean Description
    df['Description'] = df['Description'].fillna('No Description')

    # Clean Category
    valid_categories = ['Groceries', 'Utilities', 'Entertainment', 'Travel', 'Dining', 'Health', 'Shopping',
                        'Education']
    df['Category'] = df['Category'].apply(lambda x: x if x in valid_categories else 'Other')

    # Clean CustomerID
    df['CustomerID'] = df['CustomerID'].fillna('UNKNOWN')

    # Clean CustomerName
    df['CustomerName'] = df['CustomerName'].fillna('Unknown Name')

    # Clean CustomerEmail
    df['CustomerEmail'] = df['CustomerEmail'].apply(lambda x: x if '@' in x and '.' in x else 'invalid@example.com')

    # Clean CustomerPhone
    df['CustomerPhone'] = df['CustomerPhone'].apply(lambda x: x if len(x) >= 10 else '000-000-0000')

    # Clean Merchant
    df['Merchant'] = df['Merchant'].fillna('Unknown Merchant')

    # Clean MerchantLocation
    df['MerchantLocation'] = df['MerchantLocation'].fillna('Unknown Location')

    return df


# Clean the dirty CSV file
df_cleaned = clean_messy_csv('dirty_transaction_data.csv')

# Display the cleaned DataFrame head
print(df_cleaned.head())
