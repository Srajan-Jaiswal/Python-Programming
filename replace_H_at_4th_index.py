s=input("Enter:")
if(len(s)<4):
    print("Not possible")
else:
    a=len(s)
    s1=s[0:3]
    s2=s[4:a]
    print(s1+'H'+s2)
