def palin(string):
    strlen = len(string) - 1
    for i in range(int(len(string) / 2)):
        if string[i] != string[strlen]:
            return False
        else:
            strlen = strlen - 1
    return True

string = "naman"
if palin(string):
    print ("It is a palindrome")
else:
    print ("It is not a palindrome")
