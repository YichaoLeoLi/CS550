




import pandas as pd

class Element:
	def __init__(self, name, symbol, weight):
		self.atomicnumber = 0
		self.name = name
		self.symbol = symbol
		self.atomicweight = weight
		self.bp = 0
		self.mp = 0
		self.vapordensity = 0
		self.heatfusion = 0
		self.sh = 0
	def getAtomicnumber(self):
		return self.atomicnumber
	def getName(self):
		return self.name
	def getSymbol(self):
		return self.symbol
	def getAtomicweight(self):
		return self.atomicweight
	def getBp(self):
		return self.bp
	def getMp(self):
		return self.mp
	def getVapordensity(self):
		return self.vapordensity
	def getHeatfusion(self):
		return self.heatfusion
	def getSh(self):
		return self.sh
	def __str__(self):
		return "1"

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







