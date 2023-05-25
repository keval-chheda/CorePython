import array as ar

# Create an array from a list of integers
num_array = ar.array('i', (1, 10,2,3,4,5,6))
# print("num_array before update: {}".format(num_array))

# Update the elements at zeroth index
# index = 0
# num_array[index] = -1
# print("num_array after update 1: {}".format(num_array))

# Update the range of elements, say from 2-7
num_array[2:7] = ar.array('i', range(22, 27)) #22 23 24 25 26
print("num_array after update 2: {}".format(num_array))