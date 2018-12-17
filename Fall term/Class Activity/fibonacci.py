import sys
list1=[1,1]
n = float(sys.argv[1])
while len(list1)<n:
	list1.append(list1[len(list1)-1]+list1[len(list1)-2])
print(list1)