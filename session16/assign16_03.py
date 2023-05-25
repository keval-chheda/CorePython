def find_average():
    """
    Takes an unknown number of inputs and returns the average.
    """
    total = 0
    count = 0
    while True:
        try:
            num = float(input("Enter a number (or any non-numeric character to stop): "))
            total += num
            count += 1
        except:
            break

    if count == 0:
        return 0
    else:
        return total / count
print(find_average())
