# different methods to add elements in a list
# append() - it will add the element to the end of the list
# extend() - it will extend thelist of existing list by adding values of new list
# insert() - insert element before given index

list1 = ["keval", "zaid", "jay"]
print("Initial list ", list1)

new_student = input("please enter the new student name")
list1.append(new_student)
print("updated list of student", list1)

#----------------------------------------------------------------------------------------
numbers = [1,2,3,4]
print("current numbers", numbers)

num = int(input("please enter the number to add in list"))
index = 1

#numbers.insert(index, num)
numbers.insert(index, num)

print("updated numbers list", numbers)

# ------------------------------------------------------------------
# -------------------extend list example----------------------

xlist = []
xlist.extend([2,3])  #extending list
print(xlist)

xlist.extend(["example1", "example2"])
print(xlist)