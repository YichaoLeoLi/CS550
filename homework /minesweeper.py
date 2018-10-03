#Leo Li
#Description: This program creates the board for the game minesweeper. 

import random

h = int(input("\nPlease enter the height:\n>>"))
w = int(input("\nPlease enter the width:\n>>"))
b = int(input("\nPlease enter the number of bombs you want:\n>>"))
while (b<=h*w)==False:
	b = int(input("\nThere are more bombs than grids, please re-enter the number of bombs\n>>"))
n = 1
x = []
def generate():
	global n
	global x
	x = [[0]*w for i in range(h)]
	for row in x:
		for elem in row:
			print(elem, end=' ')
		print()
	while n<=b:
		j = random.randint(0,w-1)
		k = random.randint(0,h-1)
		print(k,j)
		if x[k][j]=='*':
			pass
		else:
			del x[k][j]
			x[k].insert(j,'*')
			n+=1
	for row in x:
		for elem in row:
			print(elem, end=' ')
		print()
def check():
	global x
	j = 0
	k = 0
	for k in range(h-1):
		for j in range(w-1):
			print(k,j)
			print(x)
			if x[k][j]!= '*':
				if k == 0:
					if j == 0:
						if x[0][1] == '*':
							x[0][0]+=1
						if x[1][0] == '*':
							x[0][0]+=1
						if x[1][1] == '*':
							x[0][0]+=1
					if j == (w-1):
						if x[0][w-2] == '*':
							x[0][w-1]+=1
						if x[1][w-1] == '*':
							x[0][w-1]+=1
						if x[1][w-2] == '*':
							x[0][w-1]+=1
					else:
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
				if k == (h-1):
					if j == 0:
						if x[k][1] == '*':
							x[k][0]+=1
						if x[k-1][0] == '*':
							x[k][0]+=1
						if x[k-1][1] == '*':
							x[k][0]+=1
					if j == (w-1):
						if x[k][w-2] == '*':
							x[k][j]+=1
						if x[k-1][w-1] == '*':
							x[k][j]+=1
						if x[k-1][w-2] == '*':
							x[k][j]+=1
					else:
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
				if j == 0:
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
				if j == (w-1):
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
				else:
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



generate()
check()