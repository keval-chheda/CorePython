#shalllow copy & deep copy we can use this by importing copy.

import copy

olddata = [1,2,3,[3,4,5]]
newdata = copy.copy(olddata)

olddata.append([2,3,4])
print(olddata)
print(newdata)