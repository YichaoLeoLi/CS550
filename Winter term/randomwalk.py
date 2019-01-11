

import random

counter = 0

for j in range(100):
	x = 0
	y = 0
	z = 0

	for i in range(19):
		d = random.randint(0,3)
		if d == 0:
			x+=1
		elif d == 1:
			x-=1
		elif d == 2:
			y+=1
		elif d == 3:
			y-=1

	#print(x,y)
	distance = abs(x)+abs(y)
	if distance <= 4:
		z = "walk back"
		counter+=1
	else:
		z = "public transit"
	print(distance, z, "\n", counter, "%")
