import itertools

num = ['a','b','c']
list1 = [7,8,9]
list2 = [4,5,6]

for (a,b,c) in itertools.zip_longest(num, list1, list2):
    print(a,b,c)
#
# for i, element in enumerate(list2):
#     print(element, num[i])
