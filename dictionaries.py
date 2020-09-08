map = {"srajan":123,"aman":234,"raj":543,"ram":695}
#print(dict)
for i,j in map.items():
        print(i,j)
x = map["srajan"]
print(x)
print(len(map))
for i in map:
    if(i == "ram"):
         map[i] -= 100
print(map)  
