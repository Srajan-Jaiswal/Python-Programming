x = lambda a:a*2
def func(arr,n):
    for i in (0,n-1,1):
        if(arr[i]>=3):
            arr[i] = x(arr[i])
    print(arr)       
arr=[1,5,4,5,3]
n = len(arr)
func(arr,n)  
