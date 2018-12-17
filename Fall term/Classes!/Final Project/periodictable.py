#Leo Li
#11/12/18
#the periodic table of elements
#Description: In this text-based periodic table of elements, users can view the whole table with properties, specifically the name of the element, the chemical symbol of the element, the molar mass of the element, and the atomic number of the element. It can also print out a specific element in the table if the user types either the name or the symbol of that element. Furthermore, the program can also print out the molar mass of a specific compound. However, the program cannot deal with compounds such as C12H22O11 or CO; in order to check the molar mass of CO, the user needs to type in C1O or C1O1.
#Honor Code: On my honor, I have neither given nor received any unauthorized aid. Leo Li
#Sources: https://www.dataquest.io/blog/pandas-python-tutorial/
#https://pandas.pydata.org/pandas-docs/stable/indexing.html



from elements import Element#import the Element class from the other file to store information of elements
import pandas as pd#import pandas, which allows me to import data in the csv file

ele = pd.read_csv("elements.csv")#reads the file using pandas

#Create the PeriodicTable class
class PeriodicTable:
	def __init__(self):
		self.all_elements = []#create a list that includes all the information of properties of all the elements in it
		for i in range(1, 104):#add values of properties from the file into the lists
			self.all_elements.append(Element(i,ele.index[i-1],(ele['Number'])[i-1],(ele['Symbol'])[i-1]))

	#This method allows me to print the whole table in the form of a list. With the redefined str() function in the Element class, the properties are more readable for users.
	def display_all_elements(self):
		return self.all_elements

	#This method prints out the properties of a single element
	def display_single_element(self, single):
		if isinstance(single, int) == True:#if the user input is an integer
			return self.all_elements[single-1]#return the element in the list that corresponds to that integer
		elif isinstance(single, str) == True:#if the userinput is a string
			for i in range(1,104):#try to find a element that has the name or symbol that matches the userinput, and if there is one, print information about that element
				if single == ele.index[i-1] or single == (ele['Number'])[i-1]:
					return self.all_elements[i-1]
	#This method prints out the molar mass of a compound
	def display_atomic_weight(self, compound):
		char = []#create a 2d list that stores the location and the character of a specific character. For example, for H2O, the first element in the list would be [0, H]
		num = []#a 2d list that stores the location and the integer of a specific number in the input
		weight = 0#declare weight
		word = ''#declare word
		for i in range(len(compound)):#for every single element in the string
			try:#try to convert the element at the specific location into a integer
				compound[i] = int(compound[i])
				num.append([i,compound[i]])#if it works, the store this integer to the num list
			except ValueError:#if it doesn't, store the information into the char list
				char.append([i,compound[i]])
		char.append([len(compound)+2, 0])#take another extra variable in the char list in order to check the last character digit in the user input
		num.append([100, 0])#take an extra element into the num list to avoid index error
		for i in range(len(char)-1):#check every single element in the char list
			if char[i][0]-char[i+1][0] == -1:#if the location of the first element minus the location of the second element is -1, that means the two strings are together, so the program would consider it as a single element that consisits of two letters.
				word = char[i][1] + char[i+1][1]#store the name of the element into the word variable
				for j in range(len(num)-1):#check if there is a number following the two-letter element 
					if num[j][0] == char[i][0]+2:#if there is a nunmber following
						for k in range(1,104):#check if there is a element's chemical symbol that matches with the word vairaible here
							if word == (ele['Number'])[k-1]:#If there is a match
								weight+=(ele['Symbol'])[k-1]*num[j][1]#bump the value of weight up by the molar mass of that element multiplied by the coefficient following that element
								break#break out of the loop
							else:
								if k == 103:#if the whole thing looped and there isn't a match, the user has typed wrongly
									return("\nOops...Seems you didn't enter the correct symbol of the element(notice for compounds like CO you are supposed to enter C1O1 or C1O instead of CO")
			elif char[i][0]-char[i+1][0] == -3:#If the character is at the end of the word
				word = char[i][1]#Take that single letter as an element
				for m in range(len(num)-1):#check if the character is the last thing in the list
					if len(char)-char[i][0]==1:
						for q in range (1,104):#Look for the element that matches the word variable, and bump the value of weight up by the molar mass of that element
							if word == (ele['Number'])[q-1]:
								weight+=(ele['Symbol'])[q-1]
			elif char[i][0]-char[i+1][0] == -2: #If two characters in the list has a distance of two, that means there is a number following the first element
				word = char[i][1]#set the word equal to the first letter
				for r in range(len(num)-1):
					if num[r][0] == char[i][0]+1:#If there is a number following that letter
						for l in range(1,104):#look for the element that matches the word variable, and bump the value of weight up by the molar mass of that element multiplied by the constant following it
							if word == (ele['Number'])[l-1]:
								weight+=(ele['Symbol'])[l-1]*num[r][1]
			elif char[i][0]-char[i+1][0] == -4:#if two characters in the input has a distance of 4, that means there is a number following the last string in the list
				word = char[i][1]#repeat the same thing as the previous one
				for s in range(len(num)-1):
					if len(char)-char[i][0]==1 and char[i][0]+1 == num[s][0]:
						for t in range (1,104):
							if word == (ele['Number'])[t-1]:
								weight+=(ele['Symbol'])[t-1]*(num[s][1])
		return weight #return the value of weight for printing


#the main function
def user_input():
	while True:
		x = input("\nThank you for using the text version of table of elements! To view the whole table of elements, please enter 'a'; to check specific information of an element, please enter either the name, symbol, or atomic number of the element; to check the atomic weight of a compound, please enter the formula of the chemical(However, if you want to check the atomic weight of a compound such as CO2, please type C1O2); to quit the program, please enter 'q'\n\n>>")#print out the instruction for the program
		try:#if the userinput can be converted to an integer, that means the user has entered the atomic number of an element, run the display_single_element method with input x
			x = int(x)
			print(pt.display_single_element(x))
		except ValueError:#if the user entered a string
			if x == 'a':#if it is a, then print the whole table
				print(pt.display_all_elements())
			elif x == 'q':#if it is q, then quit the program
				quit()
			elif any(char.isdigit() for char in x) == True:#if there is a number in the string, then run the atomic weight program
				x = list(x)
				print(pt.display_atomic_weight(x))
			else:#else the user has entered the name or the symbol of an element, check for the thing that matches 
				a = 0
				for i in range(1,104):
					if x == ele.index[i-1] or x == (ele['Number'])[i-1]:
						print(pt.display_single_element(x))
				if a == 103:#if the program has gone through the whole list and didn't find a match, then the user didn't type in the string correctly, show the error massage
					print("\nOops... Seems like you didn't enter the correct symbol or name... Please try again(notice for compounds like CO you are supposed to enter C1O1 or C1O instead of CO)")






pt = PeriodicTable()#set pt equal to the class


user_input()#run the main function
