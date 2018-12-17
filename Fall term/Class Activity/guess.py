import random
import math

x = random.randint(0,1000)
z = 4
def guess(): 
	global z
	print(x)
	y = (float(input("Guess the number\n>>")))
	if y == x:
		print("You win!")
	elif z == 0:
		print("You lose!!")
	elif type(y)==float:
		print("Please put in an integer!")
		guess()
	elif y > x:
		print("Try again! Your number is too big!")
		z = z - 1
		guess()
	else:
		print("Try again! Your number is too small!")
		z = z - 1
		guess()



guess()