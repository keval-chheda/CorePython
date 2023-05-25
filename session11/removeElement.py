#example to remove the element from a list remove(), discard(), del, pop()

# l1 = [1,2,3,4,5,6]
# print("intial list", l1)
#
# l1.remove(3) #it will remove the element from the list
# print(l1)

l2 = [2,3,4,7,8,9]
# l2.discard(3) #it will remove the element not the index position
print("intital list",l2)

del l2[0] # index 0 has provided to remove the element of 1st position
print(l2)

print(l2.pop(2))

