import array as arr

def removeduplicate(nums):
    return sorted(set(nums), key=nums.index)

array_numbers = arr.array('i',[1,2,3,4,4,5,6,6])
print("original array", array_numbers)

for i in range(len(array_numbers)):
    print(array_numbers[i])

result = arr.array('i', removeduplicate(array_numbers))
print(result)