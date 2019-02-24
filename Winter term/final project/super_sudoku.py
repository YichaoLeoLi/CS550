from tkinter import *

import string

import time



# Eric Li

# Feb 8, 2019





import random

import copy

import numpy as np





LBLUECOLOR = "#%02x%02x%02x" % (176,224,230) 	# https://stackoverflow.com/questions/41383849/setting-the-fill-of-a-rectangle-drawn-with-canvas-to-an-rgb-value

DBLUECOLOR = "#%02x%02x%02x" % (163,206,220)

FONTCOLOR  = "#%02x%02x%02x" % (106,90,205)

LREDCOLOR = "#%02x%02x%02x" % (255,182,193)

DREDCOLOR = "#%02x%02x%02x" % (255,105,180)





class Sudoku:

	def __init__(self, board, display):

		self.board = board

		self.display = display



	def full(self, input_board):

		for i in range(9):

			for j in range(9):

				if input_board[i][j] == 0:

					return False

		return True



	def entries(self, i, j):

		possible_entries = [0 for x in range(10)]



		for x in range(9):

			if self.board[i][x] != 0:

				possible_entries[self.board[i][x]] = 1



		for y in range(9):

			if self.board[y][j] != 0:

				possible_entries[self.board[y][j]] = 1



		horiz_block = 0

		verti_block = 0



		if 0 <= i <= 2:

			horiz_block = 0

		elif 2 < i <= 5:

			horiz_block = 3

		else:

			horiz_block = 6

		if 0 <= j <= 2:

			verti_block = 0

		elif 2 < j <= 5:

			verti_block = 3

		else:

			verti_block = 6

	

		for x in range(horiz_block, horiz_block+3):

			for y in range(verti_block, verti_block+3):

				if self.board[x][y] != 0:

					possible_entries[self.board[x][y]] = 1



		return possible_entries





	def entries_print(self, i, j, boardcopy):

		possible_entries = [0 for x in range(10)]



		for x in range(9):

			if boardcopy[i][x] != 0:

				possible_entries[boardcopy[i][x]] = 1



		for y in range(9):

			if boardcopy[y][j] != 0:

				possible_entries[boardcopy[y][j]] = 1



		horiz_block = 0

		verti_block = 0



		if 0 <= i <= 2:

			horiz_block = 0

		elif 2 < i <= 5:

			horiz_block = 3

		else:

			horiz_block = 6

		if 0 <= j <= 2:

			verti_block = 0

		elif 2 < j <= 5:

			verti_block = 3

		else:

			verti_block = 6



		for x in range(horiz_block, horiz_block+3):

			for y in range(verti_block, verti_block+3):

				if boardcopy[x][y] != 0:

					possible_entries[boardcopy[x][y]] = 1



		return possible_entries





	def valid_entries(self, possible_entries):

		valid_entries = []

		possible_entries.pop(0)



		for x in range(9):

			if possible_entries[x] == 0:

				valid_entries.append(x+1)



		random.shuffle(valid_entries)



		return valid_entries





	def solve(self):

		if self.full(self.board):

			return self.board



		else:

			i = 0

			j = 0



			for x in range(9):

				for y in range(9):

					if self.board[x][y] == 0:

						i = x

						j = y

						break



			possible_entries = self.entries(i, j)

			entries = self.valid_entries(possible_entries)



			if len(entries) != 0:

				for e in entries:

					self.board[i][j] = e

					sol=self.solve()

					if not sol:

						self.board[i][j] = 0

					else:

						return sol



	def wrong_entry(self,board_entries):

		wrong_entries = []

		wrong_entry_row = []

		wrong_entry_column = []

		wrong_entry_box = []



		for i in range(9):

			for j in range(9):

				entry = board_entries[i][j]

				error = 0



				for x in range(9):

					if self.board[i][x] != 0 and self.board[i][x]== entry:

						wrong_entry_row.append(i)

						error += 1

					if x != j:				

						if board_entries[i][x] != 0 and board_entries[i][x]== entry:

							wrong_entry_row.append(i)

							error += 1

				

				for y in range(9):

					if self.board[y][j] != 0 and self.board[y][j]== entry:

						wrong_entry_column.append(j)

						error += 1

					if y != i:				

						if board_entries[y][j] != 0 and board_entries[y][j]== entry:

							wrong_entry_row.append(i)

							error += 1



				horiz_block = 0

				verti_block = 0

				if 0 <= i <= 2:

					horiz_block = 0

				elif 2 < i <= 5:

					horiz_block = 3

				else:

					horiz_block = 6

				if 0 <= j <= 2:

					verti_block = 0

				elif 2 < j <= 5:

					verti_block = 3

				else:

					verti_block = 6



				for x in range(horiz_block, horiz_block+3):

					for y in range(verti_block, verti_block+3):

						if self.board[x][y] != 0 and self.board[x][y]== entry:

							for e in range(horiz_block, horiz_block+3):

								for g in range(verti_block, verti_block+3):

									wrong_entry_box.append([e,g])

							error += 1



						if x != i and y != j:				

							if board_entries[x][y] != 0 and board_entries[x][y]== entry:

								for e in range(horiz_block, horiz_block+3):

									for g in range(verti_block, verti_block+3):

										wrong_entry_box.append([e,g])

								error += 1

				if error != 0:

					wrong_entries.append([i,j])



		return wrong_entries, wrong_entry_box, wrong_entry_row, wrong_entry_column			





class Board:

	def __init__(self, display):

		self.display=display

		self.init_board = [[0 for x in range(9)] for x in range(9)]

		self.init_board[0] = [x for x in range(1,10)]

		random.shuffle(self.init_board[0])



	def generate(self, difficulty):

		if difficulty == 'evil':

			min_elim = 8

		elif difficulty == 'hard':

			min_elim = 7

		elif difficulty == 'medium':

			min_elim = 6

		else:

			min_elim = 5





		initial_board = Sudoku(self.init_board, self.display)

		self.init_board = initial_board.solve()





		while True:

			solutions = 1

			

			board_new = copy.deepcopy(self.init_board)



			for x in range(9):

				for y in range(random.randrange(min_elim,9)):

					indices = [x for x in range(9)]

					random.shuffle(indices)

					board_new[x][indices[y]] = 0 



			board_stored = copy.deepcopy(board_new)

			board_compare = []





			for i in range(20):

				board_test_1 = Sudoku(copy.deepcopy(board_new), self.display)

				board_solved_1 = board_test_1.solve()



				board_test_2 = Sudoku(copy.deepcopy(board_new), self.display)

				board_solved_2 = board_test_2.solve()



				if not np.array_equal(board_solved_1, board_solved_2):

					solutions += 1



				if solutions != 1:

					break



			if solutions == 1:

				break



		return board_stored





class Display: #The display class is the GUI part of the game



	def __init__(self, master):

		self.frame = Canvas(master, width = 700, height = 600, background="white")#create a canvas

		self.frame.pack()#show the canvas on the screen



		self.tiles=[]

		self.tile_states = {}



		for x in range(1,10):

			for y in range(1,10):

				upper_left = (50+51*(x-1), 50+51*(y-1))#top left coordinate of the grid

				bottom_right = (101+51*(x-1), 101+51*(y-1))#bottom right coordinate of the grid

				self.tiles.append(self.frame.create_rectangle(*upper_left, *bottom_right, fill='white', activefill = LBLUECOLOR, outline='black'))

				self.tile_states[9*(x-1)+(y-1)] = False



		self.a = "easy" #a is a difficulty option

		self.b = "intermediate"

		self.c = "hard"

		self.d = "evil"

		self.e = self.a #e is the option that gets entered into the button, to change the difficulty, just set e equal to a or b or c or d.

		self.dif_button = Menubutton(self.frame, text="easy", width = 10)#Create the difficulty button, the default difficulty is easy

		self.dif_button.menu = Menu(self.dif_button)#create the menu for difficulty button

		self.dif_button["menu"] = self.dif_button.menu

		self.dif_button.menu.add_command(label=self.a, command=self.change_easy)#add options into the difficulty button

		self.dif_button.menu.add_command(label=self.b, command=self.change_intermediate)

		self.dif_button.menu.add_command(label=self.c, command=self.change_hard)

		self.dif_button.menu.add_command(label=self.d, command=self.change_evil)

		self.dif_button.place(x=600, y=375, anchor=CENTER)#put it in the window



		self.new_game_button = Button(self.frame, text="new game", width=13, command=self.new_game)#create a new game button that starts a new game

		self.new_game_button.place(x=600,y=325,anchor=CENTER)



		self.show_solution_but = Button(self.frame, text="show solution", width=13, command=self.show_solution)#create a show solution button

		self.show_solution_but.place(x=600, y=450,anchor=CENTER)



		self.hide_solution_but = Button(self.frame, text="hide solution", width=13, command=self.hide_solution)#create a hide solution button

		self.hide_solution_but.place(x=600, y=500,anchor=CENTER)



		self.var = IntVar()

		self.note_button = Checkbutton(self.frame, text="note", variable=self.var)#create a note button(which is a check button) along with a variable to detect the state fo the button

		self.note_button.place(x=425, y=550,anchor=CENTER)



		self.check_button = Button(self.frame, text="check", width=13,command=self.check)#create a check button

		self.check_button.place(x=300, y=550,anchor=CENTER)



		initial_board = Board(self)#create a initial board from the board class

		sudoku1 = initial_board.generate('easy')#generate a easy board

		self.board_print = sudoku1#set the board for display equal to the board generated

		self.board_copy = copy.deepcopy(self.board_print)

		self.text_print_box = [[0 for x in range(9)] for x in range(9)]

		self.text_print_box_copy = [[0 for x in range(9)] for x in range(9)]

		self.show_solution_sudoku = Sudoku(self.board_print,self)


		#All of these are variables/lists that is going to be used later in the code

		self.x = 0#this variable stores the x coordinate of the place where the mouse in clicked in pixels.

		self.y = 0#this variable stores the y coordinate of the place where the mouse in clicked in pixels.

		self.char = 0#this variable is the key that is pressed on the keyborad. e.g. if you press 'e', self.char='e'

		self.pressed=False#this boolean tells you whether the mouse has been cliked or not

		self.enter_number=0#this variable will store the text creation information of the number that is entered into the board

		self.num_list = [[0]*9 for i in range(9)]#this list stores all the text creation information of the numbers in the generated sudoku

		self.entered_list = [[0 for x in range(9)] for x in range(9)]#this list stores all the text creation information of the numbers entered into the board

		self.xcord = 0#this variable stores the relative x coordinate of a number in a grid

		self.ycord = 0#this variable stores the relative y coordinate of a number in a gird

		self.enter_note=0#this variable stores the text creation information of a note that is entered

		self.note_list=[[[[0 for x in range(3)]for x in range(3)]for x in range(9)]for x in range(9)]#This list stores the text creation information of all the notes that are entered

		self.cord_copy = []#this is a copy of the relative coordinate of the location where the mouse is clicked e.g.if the mouse is clicked inside the top left grid, the list would be [0,0]

		self.note_list_copy = []#this is a copy of the note list


	#this function draws the vertical lines of the board
	def draw_vertlines(self):

		for i in [0,3,6,9]:#draw thicker lines when i = 0,3,6,9

			self.frame.create_line(50+i*51,50,50+i*51, 510,width=2)


	#this function draws the horizontal lines of the board
	def draw_horilines(self):

		for i in [0,3,6,9]:

			self.frame.create_line(50, 50+i*51, 510, 50+i*51,width=2)

	
	#This function shows the numbers on the side of the board
	def show_numbers(self):

		for i in range(1,10):

			self.frame.create_text(76+51*(i-1), 30, text=i, font='AmericanTypewriter')


	# this function shows the letters on the side of the board
	def show_letters(self):

		for i in range(1,10):

			self.frame.create_text(30, 76+51*(i-1), text=string.ascii_uppercase[i-1], font='AmericanTypewriter')


	# this function tells me the xy location of a grid inside a grid, which is going to be used for the note function later
	def x_y_location(self):

		if int(self.char)%3==1:# if the remainder of the character entered divided by 3 is 1

			self.xcord=0# the relative x coordinate in the grid would be 0

		elif int(self.char)%3==2:

			self.xcord=1

		elif int(self.char)%3==0:

			self.xcord=2

	 		

		if int(self.char)<=3:# if the character is less than or equal to 3

			self.ycord=0# the relative y coordinate would be 0

		elif int(self.char)<=6:

			self.ycord=1

		elif int(self.char)<=9:

			self.ycord=2


	# this function erases all the things on the board
	def erase_board(self):	

		for i in range(9):

			for j in range(9):

				if self.num_list[j][i]!=0:# if the number list is not equal to 0 at specific i and j, that means there is a number displayed at that location

					self.frame.delete(self.num_list[j][i])# delete the text creation information would also delete the text itself

				elif self.text_box[i][j]!=0:# else if the text list is not 0 at specific i and j, that means there is a number entered at that location

					self.frame.delete(self.text_box[i][j])# delete that text

				for k in range(3):			

					for l in range(3):			

						if self.note_list[i][j][k][l]!=0:# if the note list at specific i,j,k,l is not 0		

							self.frame.delete(self.note_list[i][j][k][l])# delete that note

		self.num_list = [[0]*9 for i in range(9)]# redefine the number list to clear all the text creation information




	# this function displays the sudoku. It puts the generated sudoku into the board
	def display_sudoku(self):

		self.text_box = [[0]*9 for i in range(9)]# define the text list

		for i in range(9):

			for j in range(9):

				if self.board_print[i][j]==0:# if the generated sudoku (in form of a list) says 0 at specific i and j, that means the grid is empty

					pass

				else:# put the number in the sudoku into the board by creating a text

					self.text = self.frame.create_text(76+51*j, 76+51*i, font=('AmericanTypewriter',20), text=self.board_print[i][j],anchor=CENTER)

					self.text_box[i][j]=self.text




	# this function changes the difficulty of the sudoku to easy
	def change_easy(self):

		self.dif_button.config(text=self.a)# when the function is activated, the text of the button would be changed to self.a(which is 'easy')

		self.e = self.a# set the difficulty to easy

		self.erase_board()# erase the whole board

		easy_board = Board(self)

		easy_board_print = easy_board.generate('easy')

		self.board_print = easy_board_print# generate a new easy board

		self.board_copy = copy.deepcopy(self.board_print)

		self.entered_list = [[0 for x in range(9)] for x in range(9)]

		self.display_sudoku()# display the new sudoku

		self.delete_solution()

		for x in range(9):

			for y in range(9):

				self.frame.itemconfig(self.tiles[9*x+y],fill="white")

				self.tile_states[9*x+y] = False


	# changes the difficulty to intermediate
	def change_intermediate(self):

		self.dif_button.config(text=self.b)

		self.e = self.b

		self.erase_board()

		intermediate_board = Board(self)

		intermediate_board_print = intermediate_board.generate('interdediate')

		self.board_print = intermediate_board_print

		self.board_copy = copy.deepcopy(self.board_print)

		self.entered_list = [[0 for x in range(9)] for x in range(9)]

		self.display_sudoku()

		self.delete_solution()

		for x in range(9):

			for y in range(9):

				self.frame.itemconfig(self.tiles[9*x+y],fill="white")

				self.tile_states[9*x+y] = False


	# changed the difficulty to hard
	def change_hard(self):

		self.dif_button.config(text=self.c)

		self.erase_board()

		self.e = self.c

		hard_board = Board(self)

		hard_board_print = hard_board.generate('hard')

		self.board_print = hard_board_print

		self.board_copy = copy.deepcopy(self.board_print)

		self.entered_list = [[0 for x in range(9)] for x in range(9)]

		self.display_sudoku()

		self.delete_solution()

		for x in range(9):

			for y in range(9):

				self.frame.itemconfig(self.tiles[9*x+y],fill="white")

				self.tile_states[9*x+y] = False


	# changes the difficulty to evil
	def change_evil(self):

		self.dif_button.config(text=self.d)

		self.erase_board()

		self.e = self.d

		evil_board = Board(self)

		evil_board_print = evil_board.generate('evil')

		self.board_print = evil_board_print

		self.board_copy = copy.deepcopy(self.board_print)

		self.entered_list = [[0 for x in range(9)] for x in range(9)]

		self.display_sudoku()

		self.delete_solution()

		for x in range(9):

			for y in range(9):

				self.frame.itemconfig(self.tiles[9*x+y],fill="white")

				self.tile_states[9*x+y] = False






	# this function starts a new game
	def new_game(self):
		# the if statements below first checks what the current difficulty is, and then generate a new board with the same difficulty
		if self.e == self.a:

			self.change_easy()

		elif self.e == self.b:

			self.change_intermediate()

		elif self.e == self.c:

			self.change_hard()

		elif self.e == self.d:

			self.change_evil()

		

		for x in range(9):

			for y in range(9):

				self.frame.itemconfig(self.tiles[9*x+y],fill="white")

				self.tile_states[9*x+y] = False


	# this function will be activated every time when the mouse is clicked
	def trace_mouse(self, event):

		self.x, self.y = event.x, event.y# set self.x and self.y equal to the location at which is mouse is clicked

		self.cord = []# define a new list which temporaily stores the information of the relative coordinate of the location at which the mouse is cliked

		for c in range(1,10):

			for d in range(1,10):

				if self.x >= 50+51*(c-1) and self.x <= 50+51*c and self.y >= 50+51*(d-1) and self.y <= 50+51*d:# is the x y location is between two lines of a grid

					for x in range(9):

						for y in range(9):

							if 9*x + y != 9*(c-1)+(d-1):

								self.frame.itemconfig(self.tiles[9*x+y],fill="white")

								self.tile_states[9*x+y] = False



					self.frame.itemconfig(self.tiles[9*(c-1)+(d-1)],fill="white" if self.board_print[d-1][c-1] != 0 or self.tile_states[9*(c-1)+(d-1)] else DBLUECOLOR)

					self.tile_states[9*(c-1)+(d-1)]	= not self.tile_states[9*(c-1)+(d-1)]

					self.frame.update()

					self.cord.append(c-1)# self.cord appends the relative x coordinate

					self.cord.append(d-1)# self.cord appends the relative y coordinate

					

					if self.tile_states[9*(c-1)+(d-1)]:

						self.pressed = True

					else:

						self.pressed = False

		

		if len(self.cord)!=0:# if the length of the cord list is not 0(the mouse is cliked outside of the sudoku board)

			self.cord_copy = self.cord# copy the list 

					


	# this function will be activated every time a key is pressed
	def trace_keyboard(self, event):

		self.char = str(event.char) # set self.char equal to the key that is pressed on the keyboard

		chars = ["1", "2", "3","4", "5", "6","7", "8", "9"]# define a list that is consisted of numbers from 1 to 9(strings)

		if self.char in chars:# if the key pressed on the keyboard is a number from 1 to 9

			if len(self.cord)!=0 and self.pressed == True and self.board_print[self.cord[1]][self.cord[0]] == 0 and self.var.get()==0:# if the length of self.cord is not 0(if the mouse is cliked inside the sudoku) and if self.pressed is true(the mouse is pressed) and if the grid that is cliked does not have a number from the sudoku on it and if the note button is note clicked

				if self.num_list[self.cord[0]][self.cord[1]] == 0: #if there is no number entered

					for i in range(3):

						for j in range(3):					

							if self.note_list[self.cord[0]][self.cord[1]][i][j]!=0:# if there are note on the grid already						

								self.frame.delete(self.note_list[self.cord[0]][self.cord[1]][i][j])	# delete all the notes					

								self.note_list[self.cord[0]][self.cord[1]][i][j]=0# reset the note list

					

					self.enter_number = self.frame.create_text(76+51*(self.cord[0]), 76+51*(self.cord
						[1]), font=('Chalkduster',20), text=self.char, fill=FONTCOLOR)

					self.frame.itemconfig(self.tiles[9*self.cord[0]+self.cord[1]],fill="white")

					self.tile_states[9*self.cord[0]+self.cord[1]] = False



					self.num_list[self.cord[0]][self.cord[1]] = self.enter_number #store the information of the entered number

					self.entered_list[self.cord[1]][self.cord[0]] = int(self.char)

					self.pressed = False





				elif self.num_list[self.cord[0]][self.cord[1]]!=0:# if there is already a number on the grid

					self.frame.delete(self.num_list[self.cord[0]][self.cord[1]])# delete that number

					self.enter_number = self.frame.create_text(76+51*(self.cord[0]), 76+51*(self.cord[1]), font=('Chalkduster',20), text=self.char, fill=FONTCOLOR)# put the new entered number on the grid

					self.frame.itemconfig(self.tiles[9*self.cord[0]+self.cord[1]],fill="white")

					self.tile_states[9*self.cord[0]+self.cord[1]] = False



					self.num_list[self.cord[0]][self.cord[1]] = self.enter_number

					self.entered_list[self.cord[1]][self.cord[0]] = int(self.char)



					self.pressed = False



			elif self.board_print[self.cord_copy[1]][self.cord_copy[0]] == 0 and self.var.get()==1: # if the grid is empty and the note function is on

				self.x_y_location()# get the relative x-y location fo the number 

				if self.num_list[self.cord_copy[0]][self.cord_copy[1]] == 0 and self.note_list[self.cord_copy[0]][self.cord_copy[1]][self.xcord][self.ycord]==0:# if there is nothing in the grid			 	

			 		self.enter_note = self.frame.create_text(76+51*(self.cord_copy[0])+51/3*(self.xcord-1), 76+51*(self.cord_copy[1])+51/3*(self.ycord-1), font=('Chalkduster',10), text=self.char, fill=FONTCOLOR) #put a note in the grid			 	

			 		self.note_list[self.cord_copy[0]][self.cord_copy[1]][self.xcord][self.ycord] = self.enter_note #store the text creation command into the note list			 	

			 		self.frame.itemconfig(self.tiles[9*self.cord_copy[0]+self.cord_copy[1]],fill="white")			 	

			 		self.tile_states[9*self.cord_copy[0]+self.cord_copy[1]] = False

			 		self.pressed = False



				elif self.num_list[self.cord_copy[0]][self.cord_copy[1]] == 0 and self.note_list[self.cord_copy[0]][self.cord_copy[1]][self.xcord][self.ycord]!=0: #if there is already a note there

					self.frame.delete(self.note_list[self.cord_copy[0]][self.cord_copy[1]][self.xcord][self.ycord])	#delete that note			

					self.note_list[self.cord_copy[0]][self.cord_copy[1]][self.xcord][self.ycord]=0# reset the note list

					self.pressed = False

			

			self.note_list_copy = self.note_list 


	#this function will be activated every time the delete button is pressed
	def trace_delete(self, event):



		if self.pressed==True and self.board_print[self.cord[1]][self.cord[0]] == 0:# if the mouse is pressed and the grid is empty orginally

			if self.num_list[self.cord[0]][self.cord[1]]!=0:# if there is a number there

				self.frame.delete(self.num_list[self.cord[0]][self.cord[1]])# delete that number

				self.num_list[self.cord[0]][self.cord[1]]=0 #reset the list

				self.entered_list[self.cord[1]][self.cord[0]] = 0

				self.frame.itemconfig(self.tiles[9*self.cord[0]+self.cord[1]],fill="white")

				self.tile_states[9*self.cord[0]+self.cord[1]] = False

				self.pressed = False

			else:

				for x in range(3):

					for y in range(3):		

						if len(self.note_list_copy)!=0:# if there is a note

							self.frame.delete(self.note_list_copy[self.cord[0]][self.cord[1]][x][y])#delete the note

							self.note_list_copy[self.cord[0]][self.cord[1]][x][y] = 0



	def check(self):

		check_board = Sudoku(self.board_print, self)

		wrong_entries, wrong_entry_box, wrong_entry_row, wrong_entry_column = check_board.wrong_entry(self.entered_list)

		if len(wrong_entries)==0:

			text = self.frame.create_text(135,550, font=('helvetica',20), text="WELL DONE!", fill=DBLUECOLOR, anchor=CENTER)

			self.frame.after(2000, lambda: self.frame.delete(text))



		for x in range(len(wrong_entry_box)):

			tile_num = 9*wrong_entry_box[x][1] + wrong_entry_box[x][0]

			self.frame.itemconfig(self.tiles[tile_num],fill=LREDCOLOR)

		

		for x in range(len(wrong_entry_row)):

			for y in range(9):

				tile_num = wrong_entry_row[x] + 9*y

				self.frame.itemconfig(self.tiles[tile_num],fill=LREDCOLOR)



		for x in range(len(wrong_entry_column)):

			for y in range(9):

				tile_num = 9*wrong_entry_column[x] + y

				self.frame.itemconfig(self.tiles[tile_num],fill=LREDCOLOR)



		for x in range(len(wrong_entries)):

			tile_num = 9*wrong_entries[x][1] + wrong_entries[x][0]

			self.frame.itemconfig(self.tiles[tile_num],fill=DREDCOLOR)



	def show_solution(self):

		for i in range(9):

			for j in range(9):

				if self.num_list[j][i]!=0:

					self.frame.delete(self.num_list[j][i])

				for k in range(3):			

					for l in range(3):			

						if self.note_list[i][j][k][l]!=0:			

							self.frame.delete(self.note_list[i][j][k][l])

							self.note_list[i][j][k][l]=0	

		self.num_list = [[0]*9 for i in range(9)]



		for x in range(9):

			for y in range(9):

				self.frame.itemconfig(self.tiles[9*x+y],fill="white")

				self.tile_states[9*x+y] = False



		if self.show_solution_sudoku.full(self.board_print):

			return self.board_print



		else:

			i = 0

			j = 0

 			

			for x in range(9):

				for y in range(9):

					if self.board_print[x][y] == 0:

						i = x

						j = y

						break

		

			possible_entries = self.show_solution_sudoku.entries_print(i, j, self.board_print)

			entries = self.show_solution_sudoku.valid_entries(possible_entries)

			if len(entries) != 0:

				for e in entries:

					self.board_print[i][j] = e



					text_print = self.frame.create_text(76+51*j, 76+51*i, font=('Chalkduster',20), text=self.board_print[i][j],anchor=CENTER,fill=FONTCOLOR)

					self.text_print_box[i][j]=text_print

					self.frame.update_idletasks()

					self.frame.after(1)

					sol=self.show_solution()

					if not sol:

						self.board_print[i][j] = 0

						self.frame.delete(self.text_print_box[i][j])

						# self.frame.update_idletasks()

						# self.frame.after(1)



					else:

						self.text_print_box_copy = copy.deepcopy(self.text_print_box)

						return sol



	def delete_solution(self):

		for i in range(9):

			for j in range(9):

				self.frame.delete(self.text_print_box_copy[j][i])

				self.text_print_box[i][j] = 0







	def hide_solution(self):

		for i in range(9):

			for j in range(9):

				self.frame.delete(self.text_print_box_copy[j][i])

				self.text_print_box[i][j] = 0

		

		self.board_print = copy.deepcopy(self.board_copy)






#put all the functions into the main function
def main():

	root = Tk()

	sudoku = Display(root)#these steps make the GUI visible

	root.bind("<Key>", sudoku.trace_keyboard)	#these three functions links the trace functions above to a mouse click, a key pressed or the delete button pressed

	root.bind("<Button-1>", sudoku.trace_mouse)

	root.bind("<BackSpace>", sudoku.trace_delete)

	# sudoku.draw_rectangle()

	sudoku.draw_vertlines()#calls the draw vertical lines function

	sudoku.draw_horilines()#calls the draw horizontal lines function

	sudoku.show_numbers()#shows the number on the side

	sudoku.show_letters()#shows the letter on the side

	sudoku.display_sudoku()#display the sudoku



	root.mainloop() #this is a function you have to call to display the GUI







main()#run the main function