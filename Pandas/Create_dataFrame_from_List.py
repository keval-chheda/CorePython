import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])

# Sample input
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

# Call the function and display the result
df = createDataframe(student_data)
print(df)
