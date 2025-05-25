import pandas as pd

# Sample DataFrame creation to simulate the input
data = {
    "employee_id": [3, 90, 9, 60, 49, 43],
    "name": ["Bob", "Alice", "Tatiana", "Annabelle", "Jonathan", "Khaled"],
    "department": [
        "Operations", "Sales", "Engineering",
        "InformationTechnology", "HumanResources", "Administration"
    ],
    "salary": [48675, 11096, 33805, 37678, 23793, 40454]
}

# Create the DataFrame
employees = pd.DataFrame(data)

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

# Call the function and print the result
print(selectFirstRows(employees))
