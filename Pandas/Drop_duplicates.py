import pandas as pd

# Sample data
data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': [
        'emily@example.com',
        'michael@example.com',
        'sarah@example.com',
        'john@example.com',
        'john@example.com',
        'alice@example.com'
    ]
}

# Create DataFrame
customers_df = pd.DataFrame(data)

# Function to remove duplicate emails
def removeDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'], keep='first')

# Apply function and print result
result_df = removeDuplicateEmails(customers_df)
print(result_df)
