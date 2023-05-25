#Write a program to subtract values in a list from
#the first element with the reduce function
from functools import reduce


# 10,1,2,3,4,5

# from functools import reduce
#
# def subtract(a, b):
#     return a - b
#
#
# list1 = [100, 1, 2,3 ,4 ,5]# 100 -1-2-3-4-5
# print (reduce(subtract, list1))

def subtract(lst):
    return reduce(lambda a, b: a - b, lst )

values = [34,4,5,6,7]
result = subtract(values)
print(result)




