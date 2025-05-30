import pandas as pd

# Function to add bonus column
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees

# Sample DataFrame
data = {
    'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
    'salary': [4548, 28150, 1103, 6593, 74576, 24433]
}

employees_df = pd.DataFrame(data)

# Call the function and print result
result_df = createBonusColumn(employees_df)
print(result_df)
