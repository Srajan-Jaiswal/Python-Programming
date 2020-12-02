a = int(input("Enter First Number"))
b = int(input("Enter Second Number"))

if a%2 == 0:
  f = open("evennum.txt", "a")
  f.write("a is even")
  f.close() 
elif a%2==1:
  f = open("oddnum.txt", "a")
  f.write("a is odd")
  f.close() 
elif b%2==0:
  f = open("evennum.txt", "a")
  f.write("b is even")
  f.close()    
elif b%2==1:
  f = open("oddnum.txt", "a")
  f.write("b is odd")
  f.close()
