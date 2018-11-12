

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

	def display_atomic_weight(self, compound):
		char = []
		num = []
		weight = 0
		word = ''
		for i in range(len(compound)):
			try:
				compound[i] = int(compound[i])
				num.append([i,compound[i]])
			except ValueError:
				char.append([i,compound[i]])
		char.append([len(compound)+2, 0])
		num.append([100, 0])
		for i in range(len(char)-1):
			number = 0
			if char[i][0]-char[i+1][0] == -1:
				word = char[i][1] + char[i+1][1]
				for j in range(len(num)-1): 
					if num[j][0] == char[i][0]+2 and num[j+1][0] != char[i][0]+3:
						for k in range(1,104):
							if word == (ele['Number'])[k-1]:
								weight+=(ele['Symbol'])[k-1]*num[j][1]
			elif char[i][0]-char[i+1][0] == -3:
				word = char[i][1]
				for m in range(len(num)-1):
					if len(char)-char[i][0]==1:
						for q in range (1,104):
							if word == (ele['Number'])[q-1]:
								weight+=(ele['Symbol'])[q-1]
			elif char[i][0]-char[i+1][0] == -2: 
				word = char[i][1]
				for r in range(len(num)-1):
					if num[r][0] == char[i][0]+1:
						for l in range(1,104):
							if word == (ele['Number'])[l-1]:
								weight+=(ele['Symbol'])[l-1]*num[r][1]
			elif char[i][0]-char[i+1][0] == -4:
				word = char[i][1]
				for s in range(len(num)-1):
					if len(char)-char[i][0]==1 and char[i][0]+1 == num[s][0]:
						for t in range (1,104):
							if word == (ele['Number'])[t-1]:
								weight+=(ele['Symbol'])[t-1]*(num[s][1])
		return weight



def user_input():
	while True:
		x = input("\nThank you for using the text version of table of elements! To view the whole table of elements, please enter 'a'; to check specific information of an element, please enter either the name, symbol, or atomic number of the element; to check the atomic weight of a compound, please enter the formula of the chemical(However, if you want to check the atomic weight of a compound such as CO2, please type C1O2); to quit the program, please enter 'q'\n\n>>")
		try:
			x = int(x)
			print(pt.display_single_element(x))
		except ValueError:
			if x == 'a':
				print(pt.display_all_elements())
			elif x == 'q':
				quit()
			elif any(char.isdigit() for char in x) == True:
				x = list(x)
				print(pt.display_atomic_weight(x))
			else:
				a = 0
				for i in range(1,104):
					if x == ele.index[i-1] or x == (ele['Number'])[i-1]:
						a+=1
						print(pt.display_single_element(x))
				if a == 0:
					print("\nOops... Seems like you didn't enter the correct symbol or name... Please try again")






pt = PeriodicTable()
#print(pt.display_all_elements())


user_input()
