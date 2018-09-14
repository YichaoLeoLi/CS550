import sys, math

m = float(sys.argv[1])
d = float(sys.argv[2])
y = float(sys.argv[3])

a = y 
b = math.floor(a + a/4 - a/100 + a/400)
c = m -2
e = math.floor((d + b + (31*c)/12)%7)

print (e)