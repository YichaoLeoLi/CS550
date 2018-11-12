




class Element:
	def __init__(self, number, name, symbol, weight):
		self.atomicnumber = number
		self.name = name
		self.symbol = symbol
		self.atomicweight = weight
	def getAtomicnumber(self):
		return self.atomicnumber
	def getName(self):
		return self.name
	def getSymbol(self):
		return self.symbol
	def getAtomicweight(self):
		return self.atomicweight
	def __str__(self):
		return "\n\nAtomicnumber: " + str(self.getAtomicnumber()) + "\nName: " + str(self.getName()) + "\nChemical symbol: " + str(self.getSymbol()) + "\nAtomicweight: " +str(self.getAtomicweight())
	__repr__ = __str__

#class PeriodicTable:
	#def __init__(self):
		#self.all_elements = []
		#self.all_elements.append(Element("Hydrogen","H",1))

	#def display_all_elements(self):
		#for i in self.all_elements:
			#print(i.atomicnumber)
			#print(i.name)
			#print(i.symbol)

#pt = PeriodicTable()
#pt.display_all_elements()

# def e(a):
# 	elements1.atomicnumber = a
# 	elements1.name = elements.index[a-1]
# 	s1 = elements['Number']
# 	elements1.symbol = s1[a-1]

# e(1)






# print(elements1.getAtomicnumber())
# print(elements1.getName())
# print(elements1.getSymbol())







