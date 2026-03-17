# CorePython

A small learning repository that contains beginner-friendly Python examples.

This project is organized into two main parts:

- **`pyhtonBasics/`**: introductory Python scripts (I/O, functions, conditionals).
- **`Pandas/`**: short pandas exercises for common DataFrame operations.

> Note: the folder name is currently `pyhtonBasics` (spelled this way in the repository).

## Repository overview

```text
CorePython/
├── pyhtonBasics/
│   ├── main.py
│   └── Calculator.py
├── Pandas/
│   ├── Change_Data_Type.py
│   ├── Create_dataFrame_from_List.py
│   ├── Create_new_column.py
│   ├── Display_first_three_row.py
│   ├── Drop_Missing_Data.py
│   ├── Drop_duplicates.py
│   ├── Modify_Columns .py
│   ├── Rename_Columns.py
│   └── Select_DATA.py
└── README.md
```

## Requirements

- Python **3.8+**
- `pandas`

Install dependency:

```bash
pip install pandas
```

## How to run scripts

From the repository root:

```bash
python pyhtonBasics/main.py
python pyhtonBasics/Calculator.py

python Pandas/Create_dataFrame_from_List.py
python Pandas/Change_Data_Type.py
python Pandas/Create_new_column.py
python Pandas/Display_first_three_row.py
python Pandas/Drop_Missing_Data.py
python Pandas/Drop_duplicates.py
python "Pandas/Modify_Columns .py"
python Pandas/Rename_Columns.py
python Pandas/Select_DATA.py
```

## Script-by-script analysis

### `pyhtonBasics/main.py`
- Simple function example with `print_hi(name)`.
- Demonstrates `if __name__ == '__main__':` entry-point usage.

### `pyhtonBasics/Calculator.py`
- Interactive CLI calculator using user input and `if/elif` operations.
- Supports `+`, `-`, `*`, `/`.
- Includes a division-by-zero check.

### `Pandas/Create_dataFrame_from_List.py`
- Creates a DataFrame from a list of lists.
- Shows setting explicit column names.

### `Pandas/Change_Data_Type.py`
- Converts a DataFrame column (`grade`) from float to int with `astype(int)`.

### `Pandas/Create_new_column.py`
- Adds a new computed column (`bonus`) based on another column (`salary`).

### `Pandas/Display_first_three_row.py`
- Uses `head(3)` to return the first three rows.

### `Pandas/Drop_Missing_Data.py`
- Removes rows with missing values in the `name` column via `dropna(subset=[...])`.

### `Pandas/Drop_duplicates.py`
- Removes duplicate rows based on `email`, keeping the first record.

### `Pandas/Modify_Columns .py`
- Updates an existing column (`salary`) by multiplying values.

### `Pandas/Rename_Columns.py`
- Renames DataFrame columns using a mapping dictionary and `rename(columns=...)`.

### `Pandas/Select_DATA.py`
- Filters rows by condition (`student_id == 101`) and selects specific columns (`name`, `age`).

## Learning outcomes

By working through this repository, a beginner can practice:

- Basic Python program structure and input handling.
- Writing small, focused functions.
- Core pandas operations: selecting, filtering, renaming, type conversion, missing data handling, duplicate removal, and column creation.

## Suggested improvements

- Fix naming consistency (e.g., `pyhtonBasics` ➜ `pythonBasics`, `Modify_Columns .py` extra space).
- Separate reusable functions from sample/demo execution blocks.
- Add automated tests (for example, with `pytest`) for each function.
- Add a `requirements.txt` file for easier setup.
