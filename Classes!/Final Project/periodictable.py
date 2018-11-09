from elements import Element
import pandas as pd

ele = pd.read_csv("elements.csv")

class PeriodicTable:
	def __init__(self):
		self.all_elements = []
		i = 1
		self.all_elements.append(Element(ele.index[i-1],(ele['Symbol'])[i-1],(ele['Symbol'])[i-1]))

	def display_all_elements(self):
		return self.all_elements

	def __str__(self):
		return "1"

pt = PeriodicTable()
print(pt.display_all_elements())
print(pt.all_elements)