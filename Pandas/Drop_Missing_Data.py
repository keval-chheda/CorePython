import pandas as pd

# Sample data with a missing value in the 'name' column
data = {
    'student_id': [32, 217, 779, 849],
    'name': ['Piper', None, 'Georgia', 'Willow'],
    'age': [5, 19, 20, 14]
}

# Create DataFrame
students_df = pd.DataFrame(data)

# Function to remove rows where 'name' is missing
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])

# Apply function and print result
result_df = dropMissingData(students_df)
print(result_df)

