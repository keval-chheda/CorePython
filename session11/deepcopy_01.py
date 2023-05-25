#deep copy creates a new object and recursively add the copies of nested object present in original elements

import copy

oldset = [[1,2,3],[3,4,5]]
newset = copy.deepcopy(oldset)

print(oldset)
print((newset))