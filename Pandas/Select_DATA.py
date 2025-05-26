import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]

# Sample data
data = {
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
}

# Create DataFrame
students_df = pd.DataFrame(data)

# Call the function
result_df = selectData(students_df)

# Print the result
print(result_df)
