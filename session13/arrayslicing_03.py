from array import *

# Create an array from a list of integers
# intger_list = (10, 14, 8, 34, 23, 67, 47, 22)
intger_array = array('i', (10, 14, 8, 34, 23, 67, 47, 22))

# Slice the given array in different situations
print("Slice array from 2nd to 6th index: {}".format(intger_array[2:6]))
print(f"Slice array from 2nd to 6th index: {intger_array[2:6]}")
print("Slice array from 2nd to 6th index: ",(intger_array[2:6]))

print("Slice last 3 elements of array: {}".format(intger_array[:-3]))
print("Slice first 3 elements from array: {}".format(intger_array[3:]))
print("Slice a copy of entire array: {}".format(intger_array[:]))