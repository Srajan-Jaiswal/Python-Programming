import math
a = 1.0
b = 5.0
c = 6.0

d = math.sqrt(b*b-4*a*c)
r1 = complex(-b-d)/2*a
r2 = complex(-b+d)/2*a
print("Root1 is {}".format(r1))
print('Root1 is {}'.format(r2))
