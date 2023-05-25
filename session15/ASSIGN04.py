def ispalindrome(string):
    leftp = 0
    rightp = len(string) - 1
    while rightp >= leftp:
        if not string[leftp] == string[rightp]:
            return False
        else:
            leftp += 1
            rightp += 1
            return True
print(ispalindrome("kaak"))

