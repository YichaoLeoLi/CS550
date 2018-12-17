#properties: hunger/thirst level, happiness, anger, energy, name, age, size
#methods(function)(method is a part of a class while function is not): run, bark,eat, sleep, play, bite 

import random

class Leo:

	#constructor
	#scale out of 100
	def __init__(self):#homework here is a variable that holds a value
		self.fullness = 5
		self.energy = 5
		self.happiness = 5
		self.homework = 0#self.homework is the class property


		#methods
	def play(self):
		if self.energy>0 and self.fullness>0:
			self.happiness+=1
			self.fullness-=1
			self.energy-=1
			status = "I played"
			return status
		else:
			status = "You played too much and you are dead :("
			return status
			quit()
		

	def playsquash(self):
		if self.energy>0 and self.fullness>0:
			self.happiness+=random.randint(-5,5)
			self.fullness-=30
			self.energy-=30
			status = "Played sqaush"
			# self.stats()
			return status
		else:
			status = "You died while playing squash because you are out of energy"
			return status
			quit()

	def stats(self):
		info + "\nenergy:" + str(self.energy)
		info += "\nfullness:" + str(self.fullness)
		info += "\nhappiness:" + str(self.happiness)
		info += "\nhappiness:" + str(self.homework)

		return info



#print(leo1.name)#accessing the property outside fo the calss

leo1 = Leo
while True:
	print(leo1.stats())
	choice = input("what would you like to do with your dog")
	if choice == "play":
		print(leo1.play())
	else:
		print("You can't do that")





