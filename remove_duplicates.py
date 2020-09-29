l = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    l.append(ele)
print(l)  
s={}
s=set()
for i in l:
    s.add(i)
print(s)    
