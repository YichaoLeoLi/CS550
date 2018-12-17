class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		
		if rank == 1:
			rank = 'Ace'
		elif rank == 11:
			rank = 'Jack'
		elif rank == 12:
			rank = 'Queen'
		elif rank == 13:
			rank = 'King'

		self.rank = rank

	def __str__(self):
		return str(self.rank) + ' of ' +str(self.suit)
