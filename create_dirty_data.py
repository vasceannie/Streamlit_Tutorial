import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()


def generate_dirty_data(num_rows=1000):
    data = {
        "TransactionID": [fake.uuid4() if random.random() > 0.1 else None for _ in range(num_rows)],
        "TransactionDate": [
            fake.date_between(start_date='-2y', end_date='today').isoformat() if random.random() > 0.1 else "31-02-2020"
            for _ in range(num_rows)],
        "Amount": [round(random.uniform(-5000, 5000), 2) if random.random() > 0.1 else "one hundred" for _ in
                   range(num_rows)],
        "Currency": [random.choice(['USD', 'EUR', 'JPY', 'GBP', 'AUD']) if random.random() > 0.1 else "DOL" for _ in
                     range(num_rows)],
        "Description": [fake.sentence(nb_words=5) if random.random() > 0.1 else None for _ in range(num_rows)],
        "Category": [random.choice(['Groceries', 'Utilities', 'Entertainment', 'Travel', 'Dining', 'Health', 'Shopping',
                                    'Education']) if random.random() > 0.1 else "Unknown" for _ in range(num_rows)],
        "CustomerID": [fake.uuid4() if random.random() > 0.1 else "" for _ in range(num_rows)],
        "CustomerName": [fake.name() if random.random() > 0.1 else "John Doe" for _ in range(num_rows)],
        "CustomerEmail": [fake.email() if random.random() > 0.1 else "invalid_email" for _ in range(num_rows)],
        "CustomerPhone": [fake.phone_number() if random.random() > 0.1 else "12345" for _ in range(num_rows)],
        "Merchant": [fake.company() if random.random() > 0.1 else None for _ in range(num_rows)],
        "MerchantLocation": [fake.address() if random.random() > 0.1 else "Nowhere" for _ in range(num_rows)]
    }
    df = pd.DataFrame(data)
    df.to_csv('dirty_transaction_data.csv', index=False)


generate_dirty_data()
print("Dirty data CSV generated successfully.")
