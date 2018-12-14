# Partner 1:
# Partner 2:
# ''' Instructions:
#   Work with a partner to complete these tasks. Assume that all variables are declared; you need only write the if-statement using the variables indicated in the description. Write your solution below the commented description.
# '''
 
# ''' 1. 
#   Variable grade is a character. If it is an A, print good work. 
# '''

import random


grade=input("\nWhat's the grade?")
if grade == "A":
   print("\ngood work")
   
# ''' 2. 
#   Variable yards is an int. If it is less than 17, multiply yards by 2. 
# '''
yards=random.randint(0,30)
if yards<17:
  yards=yards*2
  
# ''' 3. 
#   Variable success is a boolean. If something is a success, print congratulations. 
# '''
success=False
something = input("\nIs it successful?")
if something == "Yes" or  something == "yes":
  success = True
  print("Congratulations")

# ''' 4. 
#   Variable word is a String. If the string's second letter is 'f', print fun. 
# '''
 word=input("Just type something")
    
if word[1]=="f":
  print("fun")

 
# ''' 5. 
#   Variable temp is a float. Variable celsius is a boolean. If celsius is true, convert to fahrenheit, storing the result in temp. F = 1.8C + 32.
# '''
temp=float(input("Type a degree"))
degree=input("Is that temperature is Celsius or Fahrenheit?")
if degree=="Celsius":
  celsius=True
  temp = 1.8*temp+32
  print("Fahrenheit:",temp)

# ''' 6. 
#   Variable numItems is an int. Variable averageCost and totalCost are floats. If there are items, calculate the average cost. If there are no items, print no items.
# '''

numItems=int(input("How many items are there?")
if numItems==0:
  print("no items")
else:
  cost=input(float("What is the cost for this item?"))
  totalCost=cost*numItems
  averageCost=totalCost/numItems
  print("Total:",totalCost)
  print("Average:", averageCost)
  
 
# ''' 7. 
#   Variable pollution is a float. Variable cutoff is a float. If pollution is less than the cutoff, print safe condition. If pollution is greater than or equal to cutoff, print unsafe condition. 
# '''
pollution=random.random(1,500)
cutoff=random.random(1,500)
if pollution<cutoff:
  print("safe condition")
if pollution>=cutoff:
  print("unsafe condition")
  

  
#''' 8. 
#   Variable score is a float, and grade is a char. Store the appropriate letter grade in the grade variable according to this chart.
#   F: <60; B: 80-89; D: 60-69; A: 90-100; C: 70-79.
#'''
score=random.random(0,100)
if score<60:
  grade="F"
elif score<69:
  grade="D"
elif score<79:
  grade="C"
elif score<89:
  grade="B"
elif score<101:
  grade="A"
else:
  print("Error")
print("Grade:",grade)

 
# ''' 9. 
#   Variable letter is a char. If it is a lowercase letter, print lowercase. If it is an uppercase, print uppercase. If it is 0-9, print digit. If it is none of these, print symbol.
# '''
import string
letter = input("type something")
if letter.isupper() == True:
  print("uppercase")
elif letter.islower() == True:
  print("lowercase")
elif str.isdigit(letter)==True:
  print("digit")
else:
  print("symbol")
  
# ''' 10. 
#   Variable neighbors is an int. Determine where you live based on your neighbors.
#   50+: city; 25+: suburbia; 1+: rural; 0: middle of nowhere. 
# '''
neighbors=int(input("What is the population of your town?"))
if neighbors>50:
  print("city")
elif neighbors>25:
  print("suburbia")
elif neighbors>1:
  print("rural")
else:
  print("middle of nowhere")

# ''' 11. 
#   Variables doesSignificantWork, makesBreakthrough, and nobelPrizeCandidate are booleans. A nobel prize winner does significant work and makes a break through. Store true in nobelPrizeCandidate if they merit the award and false if they don't. 
# '''
sigwork=input("Does the candidate produce significant work?")
if sigwork=="yes" or sigwork=="Yes":
   doesSignificantWork=True
else:
  doesSignificantWork=False
breakthrough=input("Does the candidate make breakthroughs?")
if breakthrough=="yes" or breakthrough=="Yes":
   makesBreakthrough=True
else:
  makesBreakthrough=False
  
if doesSignificantWork=True and makesBreakthrough=True:
  nobelPrizeCandidate=True
  
# ''' 12. 
#   Variable tax is a boolean, price and taxRate are floats. If there is tax, update price to reflect the tax you must pay.
# '''
tax=False
input=input("Is there a tax?")
if input=="Yes" or input=="yes":
  tax=True
  taxrate=float(input("What is the tax rate?")
  price=tax*taxrate
  

# ''' 13.  
#   Variable word and type are Strings. Determine (not super accurately) what kind of word it is by looking at how it ends. 
#   -ly: adverb; -ing; gerund; -s: plural; something else: error   
# '''
input=input("Type a word")
if input[len(input)-1]=="y" and input[len(input)-2]=="l":
  print("adverb")
elif input[len(input)-1]=="g" and input[len(input)-2]=="n" and input[len(input)-3]=="i":
  print("gerund")
elif input[len(input)-1]=="s":
  print("plural")
else:
  print("error")
 
 
# ''' 14. 
#   If integer variable currentNumber is odd, change its value so that it is now 3 times currentNumber plus 1, otherwise change its value so that it is now half of currentNumber (rounded down when currentNumber is odd). 
# '''
 currentNumber=int(input("Type an int"))
 if currentNumber%2==1:
   currentNumber=currentNumber*3+1
else:
   currentNumber=currentNumber/2
# ''' 15. 
#   Assign true to the boolean variable leapYear if the integer variable year is a leap year. (A leap year is a multiple of 4, and if it is a multiple of 100, it must also be a multiple of 400.) 
# '''
 year=int(input("Type a year"))
 if year%4==0 and year%100==0:
  leapYear=True
 
# ''' 16. 
#   Determine the smallest of three ints, a, b and c. Store the smallest one of the three in int result. 
# '''
a=int(input("Type a number"))
b=int(input("Type a number"))
c=int(input("Type a number"))

 
# ''' 17. 
#   If an int, number, is even, a muliple of 5, and in the range of -100 to 100, then it is a special number. Store whether a number is special or not in the boolean variable special. 
# '''
 number=int(input("Type a number"))
 if number%2==0 and number%5==0 and -100<number<100:
   special=True
else:
  special=False
print(special)
 
# ''' 18. 
#   Variable letter is a char. Determine if the character is a vowel or not by storing a letter code in the int variable code.
#   a/e/o/u/i: 1; y: -1; everything else: 0
# '''
 
variablecode = 1
letter = input("enter a letter")
if letter = a or e or o or u or i:
  variablecode = 1
elif letter = y:
  variablecode = -1
else:
  variablecode = 0
 
# ''' 19. 
#   Given a string dayOfWeek, determine if it is the weekend. Store the result in boolean isWeekend.
# '''
 dayOfWeek=input("Name a day of the week")
if dayOfWeek=="Saturday" or  dayOfWeek=="saturday" or dayOfWeek=="Sunday" or dayOfWeek=="sunday":
  isWeekend=True
else:
  isWeekend=False
 
# ''' 20. 
#   Given a String variable month, store the number of days in the given month in integer variable numDays. 
# '''
 
 month = input("Enter a month number")
if int(month) == 1 or 3 or 5 or 7 or 8 or 10 or 12:
   print("31")
elif int(month) == 2 or 4 or 6 or 9 or 11:
  print("30")
else:
  print("29")
 
# ''' 21. 
#   Three integers, angle1, angle2, and angle3, supposedly made a triangle. Store whether the three given angles make a valid triangle in boolean variable validTriangle.
# '''
angle1=float(input("Angle1:"))
angle2=float(input("Angle2:"))
angle3=float(input("Angle3:"))
if angle1+angle2+angle3==180:
  validTriangle=True
else:
  validTriangle=False
 
# ''' 22. 
#   Given an integer, electricity, determine someone's monthly electric bill, float payment, following the rubric below. 
#   First 50 units: 50 cents/unit
#   Next 100 units: 75 cents/unit
#   Next 100 units: 1.20/unit
#   For units above 250: 1.50/unit, plus an additional 20% surcharge.
# '''

electricity = int(input("Please enter the number of units used this month"))
if electricity <=50:
  payment = 50*0.5
  print(payment)
elif electricity <= 150:
  payment = 25 + 0.75*(electricity - 50)
elif electricity <= 250:
  payment = 100 + 1.2*(electricity - 150)
else:
  payment = 220 + 1.5*1.2*(electricity - 250)
 
# ''' 23.
#   String, greeting, stores a greeting. String language stores the language. If the language is English, greeting is Hello. If the language is French, the greeting is Bonjour. If the language is Spanish, the greeting is Hola. If the language is something else, the greeting is something of your choice.
# '''
 
greeting = "hello"
language = "English"
if language == "English":
  print(greeting)
elif language == "French":
  greeting = "Bonjour"
  print (greeting)
elif language == "Spanish"
  greeting = "Hola"
  print(greeting)
elif language == "Chinese"
  greeting = "你好"
  print(greeting)
 
# ''' 24. 
#   Generate a phrase and store it in String phrase, given an int number and a String noun. Here are some sample phrases:
#   number: 5; noun: dog; phrase: 5 dogs
#   number: 1; noun: cat; phrase: 1 cat
#   number: 0; noun: elephant; phrase: 0 elephants
#   number: 3; noun: human; phrase: 3 humans
#   number: 1; noun: home; phrase: 3 homes
# '''
 
number = input("Please enter a number")
noun = input("Please enter a noun")
if int(number) == 1:
  print(number + noun)
else:
  print(number + noun + "s")
 
# ''' 25. 
#   If a string, userInput, is bacon, print out, "Why did you type bacon?". If it is not bacon, print out, "I like bacon." 
# '''
userInput=input("Name a food")
if "bacon" in userInput:
  print("Why did you type bacon")
else:
  print("I like bacon.")
 
# ''' 26.
#   Come up with your own creative tasks someone could complete to practice if-statements. Also provide solutions.
# '''
 
#create a variable temperature. create a boolean "coat on" . If the temperature is higher than 30 degrees celcius, take the coat off; otherwise, keep the coat on. 

coaton = True
temperature = input("enter the temperature")
if temperature >= 30:
  coaton!=coaton
 
# ''' Task 1:
 
# '''
 
# # solution
 
 
 
# ''' Task 2:
 
# '''
 
# # solution
 
 
 
# ''' Task 3:
 
# '''
 
# # solution
 
 
 
# ''' Sources
# http://www.bowdoin.edu/~ltoma/teaching/cs107/spring05/Lectures/allif.pdf
# http://www.codeforwin.in/2015/05/if-else-programming-practice.html
# Ben Dreier for pointing out some creative boolean solutions.
# '''
 
  
  