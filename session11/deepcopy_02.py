import copy

oldset = [1,2,3]
newset = copy.deepcopy(oldset)

oldset[1] = 'keval'

print(oldset)
print(newset)