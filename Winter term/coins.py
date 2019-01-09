import random

c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
for x in range(10001):
	b = 0
	for y in range(11):
		a = random.randint(0,1)
		if a == 0:
			b+=1
	if b == 0:
		c+=1
	elif b == 1:
		d+=1
	elif b == 2:
		e+=1
	elif b == 3:
		f+=1
	elif b == 4:
		g+=1
	elif b == 5:
		h+=1
	elif b == 6:
		i+=1
	elif b == 7:
		j+=1
	elif b == 8:
		k+=1
	elif b == 9:
		l+=1
	elif b == 10:
		m+=1


print(0,1,2,3,4,5,6,7,8,9,10)
print(c,d,e,f,g,h,i,j,k,l,m)
print((d+2*e+3*f+4*g+5*h+6*i+7*j+8*k+9*l+10*m)/1000,"%")

