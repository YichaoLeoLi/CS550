from elements import Element
import pandas as pd

ele = pd.read_csv("elements.csv")

class PeriodicTable:
	def __init__(self):
		self.all_elements = []
		for i in range(1, 104):
			self.all_elements.append(Element(i,ele.index[i-1],(ele['Number'])[i-1],(ele['Symbol'])[i-1]))


	def display_all_elements(self):
		return self.all_elements


	def display_single_element(self, single):
		if isinstance(single, int) == True:
			return self.all_elements[single-1]
		elif isinstance(single, str) == True:
			for i in range(1,104):
				if single == ele.index[i-1] or single == (ele['Number'])[i-1]:
					return self.all_elements[i-1]




def user_input():
	x = input("\nThank you for using the text version of table of elements! To view the whole table of elements, please enter "a"; to check specific information of an element, please either enter the name, symbol, or atomic number of the element; to check the atomic weight of a compound, please enter the formula of the chemical; to quit the program, please enter "q" ")
	while True:
		try:
			x = int(x)	
			print(type(x))
			print(pt.display_single_element(x))
		except ValueError:
			pass





pt = PeriodicTable()
#print(pt.display_all_elements())


user_input()
