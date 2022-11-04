def ispalindrome(x):
    if x == x[::-1]:
        return True
    return False

print(ispalindrome("kamalamak"))