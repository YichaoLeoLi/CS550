#a = [[1,2,3,4],[5,6]]
#del a[1][1]

#for i in range(len(a)):
#	for j in range(len(a[i])):
#		print(a[i][j], end=' ')
#	print()
#a[0].insert(0,2)
#print(a)
import random
x = [[0,0,0],[0,0,0],[0,0,0]]
j = random.randint(0,2)
k = random.randint(0,2)
print(k,j)
del x[k][j]
print(x)
x[k].insert(j,'*')
print(x)