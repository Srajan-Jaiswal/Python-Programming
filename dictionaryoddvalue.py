

def prime(num):
    for i in range(2, num):
         if num % i == 0:
            return False
    return True
def odd(num):
    if num % 2 != 0:
        return True
    return False
dict = {}
for i in range(10):
    key = int(input("key"))
    if isprime(key):
        value = int(input("value"))
        if isodd(value):
            dict[key] = value
        else:
            print("Odd")
    else:
        print("Even")
print(mydict)
