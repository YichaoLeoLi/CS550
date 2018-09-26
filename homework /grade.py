import sys

x = float(sys.argv[1])

if x < 0 or x > 5:
	print("please enter a number between 0 and 5")
elif x >= 4.85:
	print("A+")
elif x >= 4.7:
	print("A")
elif x >= 4.5:
	print("A-")
elif x >= 4.2:
	print("B+")
elif x >= 3.85:
	print("B")
elif x >= 3.5:
	print("B-")
elif x >= 3.2:
	print("C+")
elif x >= 2.85:
	print("C")
elif x >= 2.5:
	print("C-")
elif x >= 2:
	print("D+")
elif x >= 1.5:
	print("D")
elif x >= 1.0:
	print("D-")
else :
	print("F")