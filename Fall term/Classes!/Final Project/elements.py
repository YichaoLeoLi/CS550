#Leo Li
#11/12/18
#the periodic table of elements
#Description: This is the elemnt class of the periodic table that stores all the properties of the element
#Honor Code: On my honor, I have neither given nor received any unauthorized aid. Leo Li
#Sources: https://www.dataquest.io/blog/pandas-python-tutorial/
#https://pandas.pydata.org/pandas-docs/stable/indexing.html



class Element:
	def __init__(self, number, name, symbol, weight):#the element possesses atomic number, name, symbol, and the molar mass
		self.atomicnumber = number
		self.name = name
		self.symbol = symbol
		self.atomicweight = weight
	def getAtomicnumber(self):#These get function allows the user to securely get the values of the properties
		return self.atomicnumber
	def getName(self):
		return self.name
	def getSymbol(self):
		return self.symbol
	def getAtomicweight(self):
		return self.atomicweight
	def __str__(self):#define the string this way so that the string function can print out information of a single element nicely
		return "\n\nAtomicnumber: " + str(self.getAtomicnumber()) + "\nName: " + str(self.getName()) + "\nChemical symbol: " + str(self.getSymbol()) + "\nAtomicweight: " +str(self.getAtomicweight())
	__repr__ = __str__




