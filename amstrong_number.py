a=int(input("Enter the number: "))
num=a
ans=0
while(num>0):
    d = num%10
    ans+=pow(d,3)
    num = int(num/10)
if(ans==a):
    print("It's an amstrong number.")
else:
    print("It's not an amstrong number")
