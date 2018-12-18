# ''' Instructions:
#    Work with a partner to complete these tasks. You may assume that all variables/lists are declared and initialized (unless you are specifically asked to create/initialize a list); you need only write the code using the variables/lists indicated in the description. Write your solution below the commented description.
# '''
 
# ''' 1. 
#    Create a list of ints, faveNums, that holds 3 integers.
# '''
 
faveNums = []
faveNums.append(1)
faveNums.append(1)
faveNums.append(1)
print(faveNums)
 
# ''' 2. 
#    Create a list of Strings, holidays, that holds 14 holidays.  
# '''
holidays = []
holidays.append("New Year's Day")
holidays.append("New Year's Weekend")
holidays.append("Spring Festival Eve")
holidays.append("Chinese New Year")
holidays.append("Latern Festival")
holidays.append("International Women's day")
holidays.append("Arbor day")
holidays.append("Zhonghe fetival")
holidays.append("Qing Ming Jie")
holidays.append("Labor Day")
holidays.append("Youth Day")
holidays.append("Children's day")
holidays.append("Dragon Boat festival")
holidays.append("CPC founding day")

# ''' 3. 
#    Create a list of characters, grades, that holds 5 letter grades.
# '''

grades = []
grades.append("A")
grades.append("B")
grades.append("C")
grades.append("D")
grades.append("E")

# ''' 4. 
#    Create a list of booleans, funny, the can keep track of whether 18 things are funny or not. 
# '''

import random
funny = []
for i in range(19):
    a = random.randint(0,1)
    if a == 0:
        funny.append(False)
    else:
        funny.append(True)

# ''' 5. 
#    Create a list of doubles, salaries, that holds the salaries of all the employees at a university. The number of employees is stored in the int numEmployees.
# '''

salaries = [None]*10
numEmployees = random.randint(0,200)
print(len(salaries), salaries)

# ''' 6. 
#    A picture's dimensions are stored in integer variables x and y. Create a single list of integers that can store the grayscale value for each pixel in the list.
# '''
x = 10
y = 20
grayscale = [None]*x
for i in range(x):
    grayscale[i] = [None]*y

print(grayscale)

# ''' 7. 
#    In a class, each student has 0, 1, 2 or 3 siblings. The numbers of students with no siblings is stored in the variable noSiblings, the number of students with one sibling is stored in the variable oneSibling, the number of students with two siblings is stored in the variable twoSiblings, and the number of students with three siblings is stored in the variable threeSiblings. Create a list that holds all the names of the students in the class, as well as the names of all their siblings.
# '''

noSiblings = 10
oneSibling = 10
twoSiblings = 10
threeSiblings = 10
siblings = [None]*noSiblings + [None]*oneSibling + [None]*twoSiblings + [None]*threeSiblings
for i in range(noSiblings, noSiblings+oneSibling):
    siblings[i] = [None]*2
for j in range(noSiblings+oneSibling, noSiblings+oneSibling+twoSiblings):
    siblings[j] = [None]*3
for k in range(noSiblings+oneSibling+twoSiblings, noSiblings+oneSibling+twoSiblings+threeSiblings):
    siblings[k] = [None]*4
print(siblings, len(siblings))

# ''' 8. 
#    Create a list that holds all the months in the year. (No loop.)
# '''

months = []
months.append("January")
months.append("Feburary")
months.append("March")
months.append("April")
months.append("May")
months.append("June")
months.append("July")
months.append("August")
months.append("September")
months.append("October")
months.append("November")
months.append("December")

# ''' 9. 
#    Create a list that holds all the days of the week. (No loop.)
# '''
 
week = []
week.append("Monday")
week.append("Tuesday")
week.append("Wednesday")
week.append("Thursday")
week.append("Friday")
week.append("Saturday")
week.append("Sunday")
 
# ''' 10. 
#    Create a list that holds all the possible values for boolean variables. (No loop.)
# '''
 
a = []
a.append(True)
a.append(False)
 
# ''' 11. 
#    Create a list that holds the names of all the 3rd form dorms on campus. (No loop.)
# '''

dorms = ["Pitman", "Memorial", "Squire", "Nicholes"]

 
# ''' 12.  
#    Create a list that holds 3 random numbers with values between 0 and 1. (Loop optional.)
# '''

number = []
for i in range(4):
    number.append(random.randint(0,1))
 
# ''' 13. 
#    Create a list that will represent a deck of cards. Some example data for cards would be AS (ace of spaces), 5H (5 of hearts), JC (jack of clubs), 9D (9 diamonds). (Loop required.) 
# '''
 
deck = []
for suit in range(4):
   for value in range(13):
      if suit == 0:
         displaysuit = "D"
      elif suit == 1:
         displaysuit = "C"
      elif suit == 2:
         displaysuit = "H"
      else:
         displaysuit = "S"
      if value == 0:
         displayvalue = "A"
      elif value == 12:
         displayvalue = "K"
      elif value == 11:
         diplayvalue = "Q"
      elif value == 10:
         displayvalue = "J"
      else:
         displayvalue = str(value+1)
      deck.append(displayvalue+displaysuit)
 
# ''' 14. 
#    Write a Yahtzee program that simulates the rolling of five dice and prints "Yahtzee" if all five dice are the same; otherwise it should print "Try again."
# '''

dice = []
result = []
for i in range(1,7):
    dice.append(i)
for j in range(5):
    b = random.randint(1,6)
    result.append(dice[b])
if result[1] == result[2] and result[2] == result[3] and result[3] == result[4] and result[4] == result[5]:
    print("Yahtzee")
else:
    print("Try again")

# ''' 15. 
#    In a list, specials are numbers in a list that have an even number before them, an odd number behind them, and they themselves are divisible by 3. Given a list of ints called numbers, print out the location in the list of the specials, as well as the value in front of them, their value, and the value behind them. For example:
#    position 4: 14, 9, 25
# '''
 
for x in range(len(specials)):
   if specials[x]%3 == 0 and specials[x-1]%2 == 0 and specials[x+1]%2 == 1:
      print("position "+str(x)+": "+str(specials[x-1])+", "+str(specials[x])+", "+str(specials[x+1]))
 
# ''' 16. 
#    Write a program to search for the "saddle points" in a 5 by 5 list of integers. A saddle point is a cell whose value is greater than or equal to any in its row, and less than or equal to any in its column. There may be more than one saddle point in the list. Print out the coordinates of any saddle points your program finds. Print out "No saddle points" if there are none.
# '''

saddle = []
sub = []
saddle = [[None]*5 for i in range(5)]
print(saddle)
for i in range(6):
    for j in range(6):
        


# ''' 17. 
#    In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal. A chessboard can be represented by an 8 by 8 list. A 1 in the list represents a queen on the corresponding square, and a O in the list represents an unoccupied square. Given the two locations for queens (row1, col1, row2, col2), place the queens in the 2D list, chessboard. Then process the board and indicate whether or not the two queens are positioned so that they attack each other. 
# '''
 
board = [[" "]*8 for x in range(8)]
board[row1][col1] = "Q1"
board[row2][col2] = "Q2"
if row1 == row2 or col1 == col2 or (col1+row1 == col2+row2) or (cot1-row1 == col2-row2):
   attack = "true"
else:
   attack = "false"
 
# ''' 18. 
#    Given a list, write code that will reverse the order of the elements in the list. For example, dog, cat, bunny should become bunny, cat, dog.
# '''
 
elements = list(reversed(elements))
 
# ''' 19. 
#    Given a list, doorknobs, that holds strings, swap the elements at positions 1 and 3, if possible.
# '''
 
doorknobs[1], doorknobs[3] = doorknobs[3], doorknobs[1]
 
# ''' 20. 
#    In a list of ints called numbers, find the largest number in the list and place it at the end of the list.
# '''
 
number.append(number.pop(numbers.index(max(numbers))))
 
# ''' 21. 
#    In a 2D list with dimensions w by h, filled with random numbers from from 1 to 100, replace every odd number with either 2 or 22; 2 if the number was a single digit number, 22 if the number was a 2-digit number. 
# '''
 
for x in range(w):
   for y in range(h):
      if numbers[h][w]%2 == 1:
         if numbers[h][w]//10 >= 1:
            numbers[h][w] = 22
         else:
            number[h][w] = 2
 
# ''' 22. 
#    In a 2D list with dimensions w by h, holding grayscale values for an image, adjust the colors so the image is inverted. All light portions should be dark, all dark portions should be light. A value of 200 should be 5, a value of 100 should be 155, etc. Remember, there are 256 levels for color, including 0.
# '''
 
for x in range(w):
   for y in range(h):
      picture[y][x] = 255 - picture[y][x]
 
# ''' 23.
#    In a list, shifters, holding ints, shift all elements forward 1 position. For example, position 2 should move to position 1, position 1 to position 0, and position 0 to the end of the list (etc.)
# '''
 
shifternew = shifter
for x in range(len(shifter)):
   shifternew[x-1] = shifer[x]
 
# ''' 24. 
#    Given an N-by-N grid of elevation values (in meters), a peak is a grid point for which all four neighboring cells are strictly lower. Write a code fragment that counts the number of peaks in a given N-by-N grid.
# '''
 
try:
   for x in range(n):
      for y in range(n):
         if grid[n][n] > grid[n+1][n] and grid[n][n] > grid[n-1][n] and grid[n][n] > grid[n][n+1] and grid[n][n] > grid[n][n-1]:
            peaks += 1
except IndexError:
   pass  
print(peaks) 
 
# ''' 25. 
#    90% of incoming college students rate themselves as above average. Write some code that, given a list of student rankings (stored in integer list rankings), prints the fraction of values that are strictly above the average value.
# '''
 
for x in range(len(rankings)):
   if rankings[x]>average:
      fraction += 1
print(fraction/len(rankings))
 
# ''' 26. 
#    Given a 9-by-9 list of integers between 1 and 9, check if it is a valid solution to a Sudoku puzzle: each row, column, and block should contain the 9 integers exactly once.
# '''
 
puzzle = [[]*9 for x in range(9)]
for x in range(9):
   for y in range(9):
      puzzle[y][x] = random.randint(9)+1
for x in range(9):
   if puzzle[8][x] + puzzle[7][x] + puzzle[6][x] + puzzle[5][x] + puzzle[4][x] + puzzle[3][x] + puzzle[2][x] + puzzle[1][x] + puzzle[0][x] == 45 and puzzle[x][8] + puzzle[x][7] + puzzle[x][6] + puzzle[x][5] + puzzle[x][4] + puzzle[x][3] + puzzle[x][2] + puzzle[x][1] + puzzle[x][0] == 45:
      valid = 1
   else:
      valid = 0
      break
if valid = 1:
   for x in range(3):
       for y in range(3):
           if puzzle[3*x][3*y] + puzzle[3*x][3*y+1] + puzzle[3*x][3*y+2] + puzzle[3*x+1][3*y] + puzzle[3*x+1][3*y+1] + puzzle[3*x+1][3*y+2] + puzzle[3*x+2][3*y] + puzzle[3*x+2][3*y+1] + puzzle[3*x+2][3*y+2] == 45:
              valid = 1
            else:
               valid = 0
               break
 
# '''
#     27. Create a list of 100 numbers between 1 and 10 (inclusive), create a new list whose first value is the number of 1s in the original list, whose 2nd value is the number of 2s in the original list, and so on. Average the number of occurences of each number in the list over 100 repetitions. Average the averages. Print the result to the screen.
# '''
 
origin = []
new = []
for x in range(100):
   origin.append(random.randint(1,10))
for x in range (10):
   new.append(origin.index(x+1))
print(new)
 
# ''' Sources
#    http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html
#    http://introcs.cs.princeton.edu/java/14array/
# '''