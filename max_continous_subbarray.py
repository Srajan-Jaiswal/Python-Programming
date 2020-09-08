def kadanes(arr,n):
    max_till=0
    max_sum=0
    for i in range(0,n,1):
        max_sum += arr[i] 
        if(max_sum<0):
            max_sum=0
        elif(max_sum>=max_till):
            max_till=max_sum
    return max_till
n = int(input())
arr=[]
for i in range(n):
    ele=int(input())
    arr.append(ele)
print(arr)  
print(kadanes(arr,n))
