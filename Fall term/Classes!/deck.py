from cards import Card

class Deck:
	def __init__(self):
		x = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
		y = [1,2,3,4,5,6,7,8,9,10,11,12,13]
		self.z=[]
		for i in range(13):
			self.z.append(str(y[i]) + x[0])


deck1 = Deck
deck1
		


