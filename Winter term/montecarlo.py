#Leo Li
#01/11/19
#Dart simulation
#1. The most you can walk is 22 steps. Once you go to twenty, it is highly likely to get a 51% or 52%
#2. Monte Carlo simulations are basically simulations that help people to predict something that involves a lot of randomness in it. It is hard to come up with a probablity when randomness is involved, and instead of teaking an average, the monte carlo simulation can give you a better and more precise prediction. 
#3 The output of the simulation multiplied by 4 gives you pi!

import random 

a = 0

for i in range(0,10000):

	x = random.uniform(-2.0, 2.0)
	y = random.uniform(-2.0, 2.0)


	if (x**2 + y**2)**0.5 <=2:
		a+=1

print(a)
print(a/10000*4)
print(a/10000*100, "%")

