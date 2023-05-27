# //factorial of a numbers
def factoria(n):
    if n < 0:
        raise ValueError("Number should be greater than 0")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

number = 5
factorial = factoria(number)
print(factorial)