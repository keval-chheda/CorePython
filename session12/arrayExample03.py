import array as arr

numbers = arr.array('i', [1, 2, 3, 5, 7, 10])
numbers.insert(3,0)
print(numbers)

# changing 3rd to 5th element
numbers[2:5] = arr.array('i', [4, 6, 8]) #1,2,4,6,8,3,5,7,10 ..., 1,2,4,6,8
print(numbers)