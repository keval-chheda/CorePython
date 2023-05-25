# syntax for shallow copy
# copy.copy(x) ...import copy module for that

import copy

oldcollection = [[1,2,3,],[2,4,6],[3,9,27]]
newcollection = copy.copy(oldcollection)

print(oldcollection)
print(newcollection)