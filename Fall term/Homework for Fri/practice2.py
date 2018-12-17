import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

if x > y:
	if y > z:
		print("true")
	else: 
		print("false")
elif x == y:
	print("false")
elif y < z:
	print("true")
else:
	print("false")
