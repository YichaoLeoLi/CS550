#Leo Li
#09/27/18
#Description: Create a list of 15 random numbers from 0-100. Ask the user for one input from 0-100. Append this input to the list. Sort the list into descending order. 
import random
x = []
y = 0
while y<15:#take 15 random numbers
	x.append(random.randint(0,100))
	y+=1
z = int(input("\nplease enter a number between 0-100\n\n>>"))
x.append(z)
x.sort(reverse=True)#take the useer input and then reverse sort it.
print(x)