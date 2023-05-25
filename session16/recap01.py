#global scope
a = 10
def myfunction():
    a = 20
    return a
m = myfunction()
print ('a= ', m)