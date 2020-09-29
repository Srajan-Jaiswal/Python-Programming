s1=input("Enter First String: ")
s2=input("Enter Second String:")
a=len(s1)
b=len(s2)
if(b>a):
    print("Not Possible")
else:
    x=s1.find(s2)
    if(x==-1):
        print("Not Possible")
    else:
        print("Yes")
