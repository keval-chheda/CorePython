list = ["Adam", "Dean", "Harvey", "Mick", "John"]
string = "Adam lives in New York"
print ("The original list is: " + str(list))
print ("The original string is: " + string)

result = any(item in string for item in list)
print ("Does the string contain 'Adam': " + str(result))