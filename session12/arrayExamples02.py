import array as arr
# a = arr.array('i', [2, 4, 6, 8])
# print("First element:", a[0])
# print("Second element:", a[1])
# print("Second last element:", a[-1]) #8


# Write a python program to get the number of occurrences of a specified element in an array.
a = arr.array('i',[1,2,3,2,3,3,5,67,7])
element = 67

def count_occurences(arr, number):
    count = 0
    for item in arr:
        if item == number:
            count = count + 1
    return count

result = count_occurences(a, element)
print(result)



