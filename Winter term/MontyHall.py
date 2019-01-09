#Leo Li
#01/09/19
#Monty Hall simulation
#Description: This program runs the simulation for mounty hall problem
#So I actually know the solution to this problem because I have done it in my middle school. The solution is pretty couterintuive. Most people would think the chance of getting the car is 50-50 because you have two choices and you have to choose one, which gives you 1/2 = 50%. This makes a lot sense, but the most ignored part is the first choice that you have made. The solution can actually be derived from the code below. Assume you always change your choice, then the only way you can get the car is by selecting a door that has a penny behind it. Therefore, the probablity that you'll get the car if you always change your opinion should be the same as the probablity of choosing a door with a penny behind it the first time, which is 2/3 = 66.7%
#Honor Code: On my honor, I have neither given nor received any unauthorized aid



import random
#This is the part where you always switch the door
e = 0
f = 0
for i in range(1, 100000):
	d = random.randint(1,3)

	print(d)
	if d == 1:
		d = 1
	elif d == 2:
		d = 1
	elif d == 3:
		d = 2
	
	if d == 1:
		d = 2
	elif d == 2:
		d = 1
	
	if d == 2:
		e+=1
	f+=1

	print(e,f)
	print(e/f)
#This is the part where you always don't switch

e = 0
f = 0
for i in range(1, 1000):
	d = random.randint(1,3)

	print(d)
	if d == 1:
		d = 1
	elif d == 2:
		d = 1
	elif d == 3:
		d = 2
	

	
	if d == 2:
		e+=1
	f+=1

	print(e,f)
	print(e/f)