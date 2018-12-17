#Leo Li
#09/27/18
#Description: Task of this program is to generate a list with 10 random numbers ranging from 0 to 100, and then delete any numbers in the list that is divisible by 3. Then print the list in descending order
import random

x = []
y = 0
z = 0
for y in range(10):#add random numbers into the list 10 times
	x.append(random.randint(0,100))
	y+=1
x.sort(reverse=True)#sort the list, and then reverse it
while z<len(x):#check numbers in list that are divisible by 3, then delete it
	if x[z]%3==0:
		del x[z]
	else:
		z+=1
print(x)