#Leo Li
#Sep. 23
#This is guessing game in which the player has to guess the number that the system automatically generates. The player has 7 chances, and the system would make different suggestions according to how far is the user input away from the correct answer. When the game is finished, player can choose to play again or end the game.
#On my honor, I have neither given nor received any unauthorized aid.
import random
import time
#---------------------------------------------------------------
def start():
	while True:
		try:
			x = random.randint(200, 900)#system chooses a number between 200 and 900
			y = 7
			print("\nA random number is being generated")
			print("\n......")
			time.sleep(1)#I used time delay function throughout the game to show that the system is "Processing", and just to make better user experience
			print("\n......")
			time.sleep(1)
			print("\nthe random number is now generated,")
			while y>0:  #y repersents number of lives remaining, and this while loops allows the program to keep running while the lives are greater than 0
				result = int(input("\nplease guess the number:\n\n>>"))
				if result == x: #If the user get the number right, the computer tell the user he/she wins, and if he/she wants to start another one
					print("\nchekcking...")
					time.sleep(1.5)
					print("\nauthenticating...")
					time.sleep(1.5)
					print("\n......")
					time.sleep(1)
					print("\n......")
					time.sleep(1)
					print("\nThe number is correct! You win!")
					z = int(input("\nPlay again?\n1)Yes\n2)No\n\n>>"))
					if z == 1:
						start()
					break
				if result < x: #if the user input is less than the number, the program makes different suggestions based on the difference between the user input and the actual number
					if x>(300+result):
						print("\nchecking...")
						time.sleep(1.5)
						print("\n......")
						time.sleep(1)
						print("\n......")
						time.sleep(1)
						print("\nYour answer is far from being correct! It is way smaller than the correct answer")
						y-=1
						print("Lives remaining:", y)
					elif x>(150+result):
						print("\nchecking...")
						time.sleep(1.5)
						print("\n......")
						time.sleep(1)
						print("\n......")
						time.sleep(1)
						print("\nYour answer is much smaller than the number")
						y-=1
						print("Lives remaining:", y)
					elif x>(100+result):
						print("\nchecking...")
						time.sleep(1.5)
						print("\n......")
						time.sleep(1)
						print("\n......")
						time.sleep(1)
						print("\nYour answer is close to the number; it is smaller than the number by less than 150")
						y-=1
						print("Lives remaining:", y)
					elif x>(50+result):
						print("\nchecking...")
						time.sleep(1.5)
						print("\n......")
						time.sleep(1)
						print("\n......")
						time.sleep(1)
						print("\nYour answer is pretty close to the correct answer; it is smaller than the number by less than 100")
						y-=1
						print("Lives remaining:", y)
					elif x>(20+result):
						print("\nchecking...")
						time.sleep(1.5)
						print("\n......")
						time.sleep(1)
						print("\n......")
						time.sleep(1)
						print("\nYou are so close right now...; your answer is smaller than the number by less than 50")
						y-=1
						print("Lives remaining:", y)
					elif x>(0.2+result):
						print("\nchecking...")
						time.sleep(1.5)
						print("\n......")
						time.sleep(1)
						print("\n......")
						time.sleep(1)
						print("\nYou are so close! If you can just add a little bit more...")
						y-=1
						print("Lives remaining:", y)
				if result > x: #Same thing when the user input is greater than the number
					if result>(300+x):
						print("\nchecking...")
						time.sleep(1.5)
						print("\n......")
						time.sleep(1)
						print("\n......")
						time.sleep(1)
						print("\nYour answer is far from being correct! It is way larger than the correct answer")
						y-=1
						print("Lives remaining:", y)
					elif result>(150+x):
						print("\nchecking...")
						time.sleep(1.5)
						print("\n......")
						time.sleep(1)
						print("\n......")
						time.sleep(1)
						print("\nYour answer is much larger than the number")
						y-=1
						print("Lives remaining:", y)
					elif result>(100+x):
						print("\nchecking...")
						time.sleep(1.5)
						print("\n......")
						time.sleep(1)
						print("\n......")
						time.sleep(1)
						print("\nYour answer is close to the number; it is larger than the number by less than 150")
						y-=1
						print("Lives remaining:", y)
					elif result>(50+x):
						print("\nchecking...")
						time.sleep(1.5)
						print("\n......")
						time.sleep(1)
						print("\n......")
						time.sleep(1)
						print("\nYour answer is pretty close to the correct answer; it is larger than the number by less than 100")
						y-=1
						print("Lives remaining:", y)
					elif result>(20+x):
						print("\nchecking...")
						time.sleep(1.5)
						print("\n......")
						time.sleep(1)
						print("\n......")
						time.sleep(1)
						print("\nYou are so close right now...; your answer is larger than the number by less than 50")
						y-=1
						print("Lives remaining:", y)
					elif result>(0.2+x):
						print("\nchecking...")
						time.sleep(1.5)
						print("\n......")
						time.sleep(1)
						print("\n......")
						time.sleep(1)
						print("\nYou are so close! If you can just reduce it by a little bit...")
						y-=1
						print("Lives remaining:", y)
				if y == 0: #When the user used all their chances, the program tells the user the real answer, and if they want to start another one
					print("\ncheking number of lives remaining......")
					time.sleep(1.5)
					print("\n......")
					time.sleep(1)
					print("\n......")
					time.sleep(1)
					print("\n......")
					time.sleep(1)
					print("\nlooks like you are dead...")
					time.sleep(1)
					print("\n......")
					time.sleep(1)
					print("\n......")
					time.sleep(1)
					print("The answer is",x)
					time.sleep(1)
					print("\ngame over")
					z = int(input("\nPlay again?\n1)Yes\n2)No\n\n>>"))
					if z == 1:
						start()
			break
		except ValueError: #The except and the big "while True" loop and "try:" together makes it possible that when the user doesn't enter an integer, the program would tell the user to enter an integer
			print("\n\nThat's not an integer, please try again")
		z = int(input("\nTry again?\n1)Yes\n2)No\n\n>>"))
		if z == 1:
			start()
start()