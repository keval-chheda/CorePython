import copy

olddata = [[1,2,3,],[2,4,6],[5,6,7]]
newdata = copy.copy((olddata))

olddata [1][1] = 'nb'

print(olddata)
print(newdata)