import os
fo = open("C:/Users/admin/Desktop/TextDocument1.txt", "r+")
str = fo.read(10);
print ("Read String is : ", str)
fo.close()

# os.rename("C:/Users/admin/Desktop/TextDocument.txt", "C:/Users/admin/Desktop/TextDocument1.txt")

print(os.getcwd())
