import pandas as pd

def convertGradeToInt(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

data = {
    'student_id': [1, 2],
    'name': ['Ava', 'Kate'],
    'age': [6, 15],
    'grade': [73.0, 87.0]
}

students = pd.DataFrame(data)
result = convertGradeToInt(students)
print(result)

