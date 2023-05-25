import array

arr1 = array.array('i', [1,2,3])
arr2 = array.array('i',[4,5,6])
#concatenate
#insert
#append
#extend

print(arr1)
print(arr2)

# arr3 = arr1 + arr2
# print(arr3)
#
arr1.append(7)
print(arr1)

arr2.insert(0,3)
print(arr2)

# arr1.extend(arr2)
# print(arr1)