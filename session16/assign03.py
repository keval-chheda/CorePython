def avgfun(*n):
    sums = 0

    for i in n:
        sums = sums + i
    avg = sums / len(n)
    return avg

result = avgfun(1,2,3)
print(round(result, 3))