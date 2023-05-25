num1, num2 = 0, 1
print("Fibonacci Series")

for i in range(1, 11):
    print(num1, end = " ")
    res = num1 + num2
    num1 = num2
    num2 = res

print(res)