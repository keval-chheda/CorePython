#lambda expression : - it is a annonymous function

lists = [1,2,3,4,5,6,7,8,9]

# def isgreater_than2(num):
#     return num > 2

filtered_list = list(filter(lambda x: x > 2, lists))
print(filtered_list)