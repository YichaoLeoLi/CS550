import random
import matplotlib.pyplot as plt




result = [0]*52000


for i in range(10000):
	x = 0
	y = 0
	z = 0
	c = 0
	x = random.randint(1,13)
	for k in range(x):
		y = random.randint(1,8)
		for j in range(y):
			z = random.randint(40,500)
			c += z
	for l in range(1, 52000):
		if c == l:
			result[l]+=1
	print(c)


plt.plot(result)
plt.show()





