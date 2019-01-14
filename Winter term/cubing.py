import random
import math
import matplotlib.pyplot as plt
from collections import Counter

l2c = 16.65

f4c = 0
f8e = 0
l4e = 0
three = 0

stat = []

for i in range(10000):
	result = 0
	f4c = random.uniform(104.64,180)
	for j in range(math.floor(f4c)):
		f8e = random.uniform(150,183.2)
		for k in range(math.floor(f8e)):
			l4e = random.uniform(40,120)
			for l in range(math.floor(l4e)):
				three = random.uniform(20,35)

	print(f4c, f8e, l4e, three, f4c+l2c+f8e+l4e+three)
	result = math.floor(f4c+l2c+f8e+l4e+three)
	stat.append(result)


stats = sorted(Counter(stat).items())
print(stats)
y = []
x = []
for tuples in stats:
	y.append(tuples[1])
	x.append(tuples[0]/60)
print(y,x)


plt.plot(x,y)
plt.show()




