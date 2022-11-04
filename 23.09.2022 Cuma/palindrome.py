def ispalindrome(x):
    soldan = 0
    sagdan = len(x) - 1 

    while sagdan >= soldan:
        if not x[sagdan] == x[soldan]:
            return False
        soldan +=1
        sagdan -= 1
    return True

print(ispalindrome("mouse"))


    