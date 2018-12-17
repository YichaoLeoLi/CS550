#Leo Li
#Description: This is the minesweeper game. 
#10/08/18
#Honor code: I have neither given nor received any unauthorized aid. Leo
#Sources: Eric Li helped me with the project

import random
import sys

print("\nWelcome to the minesweepr game! The coordinate system for this minesweeper game works in a way that the top left corner has a coordinate of [1, 1], and the point to the right of that has a coordinate of [0, 2], and the point below that has a coordinate of [2, 0], and so on. Flags in this game will be represented by $, and x represents spaces that are not yet revealed.")
h = int(input("\nPlease enter the height:\n>>"))
w = int(input("\nPlease enter the width:\n>>"))
b = int(input("\nPlease enter the number of bombs you want:\n>>"))

while (b<=h*w)==False:
	b = int(input("\nThere are more bombs than grids, please re-enter the number of bombs\n>>"))
n = 1
x = []
y = []
def p():#print the answer key 
	for row in x:
		for elem in row:
			print(elem, end=' ')
		print()
def p1():#print the original list
	for row in y:
		for elem in row:
			print(elem, end=' ')
		print()
def blankboard():#generate the original 2d list 
	global y
	y = [["x"]*w for i in range(h)]
def userinput():#user's input of the space that they want to reveal
	global x,y,c,d 
	choice = input("\nPlease enter the coordinate of the space you want to reveal (If you want to reveal space in row 2 and column 3, enter 2 3)\n>>")
	choice1 = choice.split()
	c = int(choice1[0])-1
	d = int(choice1[1])-1
def flag():#user's input of the position of the flag they want to reveal
	global x,y,c,d
	choice = input("\nPlease enter the coordinate of the space you want to reveal or flag(To put a flag on a space, for example, if you want to put a flag on space row 2 and column 3, enter 2 3 f)\n>>")
	choice1 = choice.split()
	c = int(choice1[0])-1
	d = int(choice1[1])-1
	if len(choice1)==3:
		y[c][d]='$'
	else:
		y[c][d]=x[c][d]
def generate():#generate the answer key
	global n, x, c, d
	x = [[0]*w for i in range(h)]
	while n<=b:#while the number of bombs already put in is smaller than the number of bombs designated, keep running the code
		j = random.randint(0,w-1)
		k = random.randint(0,h-1)
		if x[k][j]=='*' or (k==c and j==d):#if there is already a bomb in the space or if it is the position that the player first wanted to reveal, run the loop again
			pass
		else:#put a bomb in and bump the value of n up by 1
			del x[k][j]
			x[k].insert(j,'*')
			n+=1
def check():
	global x
	j = 0
	k = 0
	for k in range(h):
		for j in range(w):#these two for loops make the program do things in the loop until every space in the answer key board is checked
			if x[k][j]!= '*':#if the space is not a bomb
				if k == 0:#if it is in the first row
					if j == 0:#if space is on the top left hand corner, check for bombs around it. If there is a bomb, add the value of the space by 1.
						if x[0][1] == '*':
							x[0][0]+=1
						if x[1][0] == '*':
							x[0][0]+=1
						if x[1][1] == '*':
							x[0][0]+=1
					elif j == (w-1):#top right hand corner
						if x[0][w-2] == '*':
							x[0][w-1]+=1
						if x[1][w-1] == '*':
							x[0][w-1]+=1
						if x[1][w-2] == '*':
							x[0][w-1]+=1
					else:#anywhere else in the first row
						if x[0][j-1] == '*':
							x[0][j]+=1
						if x[0][j+1] == '*':
							x[0][j]+=1
						if x[1][j-1] == '*':
							x[0][j]+=1
						if x[1][j] == '*':
							x[0][j]+=1
						if x[1][j+1] == '*':
							x[0][j]+=1
				if k == (h-1):#if the space is in the bottom row
					if j == 0:#bottom left
						if x[k][1] == '*':
							x[k][0]+=1
						if x[k-1][0] == '*':
							x[k][0]+=1
						if x[k-1][1] == '*':
							x[k][0]+=1
					elif j == (w-1):#bottom right
						if x[k][w-2] == '*':
							x[k][j]+=1
						if x[k-1][w-1] == '*':
							x[k][j]+=1
						if x[k-1][w-2] == '*':
							x[k][j]+=1
					else:#bottom line
						if x[k][j-1] == '*':
							x[k][j]+=1
						if x[k][j+1] == '*':
							x[k][j]+=1
						if x[k-1][j-1] == '*':
							x[k][j]+=1
						if x[k-1][j] == '*':
							x[k][j]+=1
						if x[k-1][j+1] == '*':
							x[k][j]+=1
				if j == 0:#leftmost line
					if k!=0 and k!=(h-1):
						if x[k+1][j] == '*':
							x[k][j]+=1
						if x[k][j+1] == '*':
						    x[k][j]+=1
						if x[k-1][j+1] == '*':
							x[k][j]+=1
						if x[k-1][j] == '*':
							x[k][j]+=1
						if x[k+1][j+1] == '*':
							x[k][j]+=1
				if j == (w-1):#rightmost line
					if k!=0 and k!=(h-1):
						if x[k+1][j] == '*':
							x[k][j]+=1
						if x[k][j-1] == '*':
						    x[k][j]+=1
						if x[k-1][j-1] == '*':
							x[k][j]+=1
						if x[k-1][j] == '*':
							x[k][j]+=1
						if x[k+1][j-1] == '*':
							x[k][j]+=1
				if j!= 0 and j!= (w-1):#anywhere in the middle
					if k!= 0 and k!= (h-1):
						if x[k][j-1] == '*':
							x[k][j]+=1
						if x[k][j+1] == '*':
							x[k][j]+=1
						if x[k-1][j-1] == '*':
							x[k][j]+=1
						if x[k-1][j] == '*':
							x[k][j]+=1
						if x[k-1][j+1] == '*':
							x[k][j]+=1
						if x[k+1][j-1] == '*':
							x[k][j]+=1
						if x[k+1][j] == '*':
							x[k][j]+=1
						if x[k+1][j+1] == '*':
							x[k][j]+=1
def reveal():
	global x,y,c,d
	if x[c][d]!='*' and x[c][d]!=0:#if the space is not 0 or a bomb, reveal that single number	
		y[c][d]=x[c][d]
		p1()
		flag()
		win()
		reveal()
	elif x[c][d]=='*' and y[c][d]!='$':#if the space is a bomb, end the game
		p1()
		print("Game Over!")
		sys.exit()
	elif y[c][d]=='$':
		p1()
		flag()
		win()
		reveal()
	elif x[c][d]==0:#if the space is 0, run the following:
		space()
		flag()
		win()
		reveal()

def space():#This function deals with revealing contiguous '0' tiles
	global x,y,c,d
	check = []
	check1 = []
	check.append([c,d])
	check1.append([c,d])

	while len(check)!=0:
		x1 = check[0][0]
		y1 = check[0][1]

		y[x1][y1] = x[x1][y1]

		for i in range(-1,2):
			for j in range(-1,2):
				if x1+i>=0:
					if x1+i<=(h-1):
						if y1+j>=0:
							if y1+j<= (w-1):
								if [i,j]!=[0,0]:
									y[x1+i][y1+j]=x[x1+i][y1+j]
									if x[x1+i][y1+j] == 0 and [x1+i, y1+j] not in check1:
										check.append([x1+i,y1+j])
										check1.append([x1+i,y1+j])
		check.pop(0)
	p1()


def win():
	global x,y,c,d
	j = 0
	k = 0
	a = 0
	e = 0
	for j in range(h):
		for k in range(w):
			if y[j][k]!="x":
				if y[j][k]=="$":
					if x[j][k]=="*":
						a+=1
						if a == b:
							p1()
							print("\nCongratulation! You win!")
							sys.exit()

def main():
	global blankboard, userinput, generate, check, reveal
	blankboard()
	userinput()
	generate()
	check()
	reveal()


main()