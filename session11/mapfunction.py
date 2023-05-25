#[1,2,3,4,5]
#[2,4,9,16,25] "..square of a elemnt present inside a list

# def square(n):
#     return n*n

my_list = [1,2,3,4,5]
updated_list = map(lambda x: x*x, my_list) #map(function, object)

# print(updated_list)
print(list(updated_list))