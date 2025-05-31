import pandas as pd

# Input Data
data = {
    'name': ['Jack', 'Piper', 'Mia', 'Ulysses'],
    'salary': [19666, 74754, 62509, 54866]
}

# Create DataFrame
employees = pd.DataFrame(data)

# Function to double the salary
def modifySalary(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees

# Apply function and print the result
updated_employees = modifySalary(employees)
print(updated_employees)
