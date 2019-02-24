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

		# self.text_print_box = [[0 for x in range(9)] for x in range(9)]

		# self.board_copy = copy.deepcopy(self.board)

		# self.text_print_box_copy = [[0 for x in range(9)] for x in range(9)]



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





	# def solve_print(self, show_hide):

	# 	if show_hide == 'show':

	# 		if self.full(self.board_copy):

	# 			return self.board_copy



	# 		else:

	# 			i = 0

	# 			j = 0

	 			

	# 			for x in range(9):

	# 				for y in range(9):

	# 					if self.board_copy[x][y] == 0:

	# 						i = x

	# 						j = y

	# 						break

			

	# 			possible_entries = self.entries_print(i, j, self.board_copy)

	# 			entries = self.valid_entries(possible_entries)

	# 			if len(entries) != 0:

	# 				for e in entries:

	# 					self.board_copy[i][j] = e



	# 					text_print = self.display.frame.create_text(76+51*j, 76+51*i, font=('Chalkduster',20), text=self.board_copy[i][j],anchor=CENTER,fill=FONTCOLOR)

	# 					self.text_print_box[i][j]=text_print

	# 					# self.display.frame.update_idletasks()

	# 					# self.display.frame.after(1)

	# 					# sudoku.frame.create_text

	# 					sol=self.solve_print('show')

	# 					if not sol:

	# 						self.board_copy[i][j] = 0

	# 						self.display.frame.delete(self.text_print_box[i][j])

	# 						# self.display.frame.update_idletasks()

	# 						# self.display.frame.after(1)



	# 					else:

	# 						text_print_box_copy = copy.deepcopy(self.text_print_box)

	# 						return sol

		

		

	# 	elif show_hide == 'hide':

	# 		print(text_print_box_copy)



	# 		for i in range(9):

	# 			for j in range(9):

	# 				# if self.text_print_box[i][j]!=0:

	# 				self.display.frame.delete(self.text_print_box_copy[j][i])



	# 		self.text_print_box = [[0 for x in range(9)] for i in range(9)]



	# 		print('hi')



	# def hide_print(self):

	# 	print(self.text_print_box)

	# 	for i in range(9):

	# 		for j in range(9):

	# 			if self.text_print_box[i][j]!=0:

	# 				self.display.frame.delete(self.text_print_box[j][i])



	# 	self.text_print_box = [[0 for x in range(9)] for i in range(9)]

	# 	print('Hi')



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



				# print(i,j)



		return wrong_entries, wrong_entry_box, wrong_entry_row, wrong_entry_column

		# return(self.board)

			





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



# class Tile:



# 		else:

# 			return super().create_rectangle(*args, **kwargs)

# 	def __init__(self,canvas,p1,p2,loc,inputmode=False,state=0):



# 		self.canvas=canvas

# 		self.repr=str(self.canvas.create_rectangle(p1,p2,loc=loc,activefill=LBLUECOLOR if inputmode else "white",fill=DBLUECOLOR if state else "white"))



# 	def __repr__(self):

# # 		return self.repr



class Display:



	def __init__(self, master):

		self.frame = Canvas(master, width = 700, height = 600, background="white")

		self.frame.pack()



		self.tiles=[]

		self.tile_states = {}



		for x in range(1,10):

			for y in range(1,10):

				upper_left = (50+51*(x-1), 50+51*(y-1))

				bottom_right = (101+51*(x-1), 101+51*(y-1))

				# upper_left = (50+50*(x-1), 50+51.3*(y-1))

				# bottom_right = (101.3+51.3*(x-1), 101.3+51.3*(y-1))

				self.tiles.append(self.frame.create_rectangle(*upper_left, *bottom_right, fill='white', activefill = LBLUECOLOR, outline='black'))

				self.tile_states[9*(x-1)+(y-1)] = False



		self.a = "easy"

		self.b = "intermediate"

		self.c = "hard"

		self.d = "evil"

		self.e = self.a

		self.dif_button = Menubutton(self.frame, text="easy", width = 10)

		self.dif_button.menu = Menu(self.dif_button)

		self.dif_button["menu"] = self.dif_button.menu

		self.dif_button.menu.add_command(label=self.a, command=self.change_easy)

		self.dif_button.menu.add_command(label=self.b, command=self.change_intermediate)

		self.dif_button.menu.add_command(label=self.c, command=self.change_hard)

		self.dif_button.menu.add_command(label=self.d, command=self.change_evil)

		self.dif_button.place(x=600, y=400, anchor=CENTER)



		self.new_game_button = Button(self.frame, text="new game", width=13, command=self.new_game)

		self.new_game_button.place(x=600,y=350,anchor=CENTER)



		self.show_solution_but = Button(self.frame, text="show solution", width=13, command=self.show_solution)

		self.show_solution_but.place(x=600, y=450,anchor=CENTER)



		self.hide_solution_but = Button(self.frame, text="hide solution", width=13, command=self.hide_solution)

		self.hide_solution_but.place(x=600, y=500,anchor=CENTER)



		self.var = IntVar()

		self.note_button = Checkbutton(self.frame, text="note", variable=self.var)

		self.note_button.place(x=400, y=550,anchor=CENTER)



		self.check_button = Button(self.frame, text="check", width=13,command=self.check)

		self.check_button.place(x=300, y=550,anchor=CENTER)



		initial_board = Board(self)

		sudoku1 = initial_board.generate('easy')

		# self.sudoku1 = [[0,0,3,0,2,0,6,0,0],[9,0,0,3,0,5,0,0,1],[0,0,1,8,0,6,4,0,0],[0,0,8,1,0,2,9,0,0],[7,0,0,0,0,0,0,0,8],[0,0,6,7,0,8,2,0,0],[0,0,2,6,0,9,5,0,0],[8,0,0,2,0,3,0,0,9],[0,0,5,0,1,0,3,0,0]]

		self.board_print = sudoku1

		self.board_copy = copy.deepcopy(self.board_print)

		self.text_print_box = [[0 for x in range(9)] for x in range(9)]

		# self.board_copy = copy.deepcopy(self.board)

		self.text_print_box_copy = [[0 for x in range(9)] for x in range(9)]

		self.show_solution_sudoku = Sudoku(self.board_print,self)



		self.x = 0

		self.y = 0

		self.char = 0

		self.pressed=False

		self.enter_number=0

		self.num_list = [[0]*9 for i in range(9)]

		self.entered_list = [[0 for x in range(9)] for x in range(9)]

		self.xcord = 0

		self.ycord = 0

		self.enter_note=0

		self.note_list=[[[[0 for x in range(3)]for x in range(3)]for x in range(9)]for x in range(9)]

		self.cord_copy = []

		self.note_list_copy = []



	def draw_vertlines(self):

		for i in [0,3,6,9]:

			self.frame.create_line(50+i*51,50,50+i*51, 510,width=2)



	def draw_horilines(self):

		for i in [0,3,6,9]:

			self.frame.create_line(50, 50+i*51, 510, 50+i*51,width=2)

	

	def show_numbers(self):

		for i in range(1,10):

			self.frame.create_text(76+51*(i-1), 30, text=i, font='AmericanTypewriter')



	def show_letters(self):

		for i in range(1,10):

			self.frame.create_text(30, 76+51*(i-1), text=string.ascii_uppercase[i-1], font='AmericanTypewriter')



	def x_y_location(self):

		if int(self.char)%3==1:

			self.xcord=0

		elif int(self.char)%3==2:

			self.xcord=1

		elif int(self.char)%3==0:

			self.xcord=2

	 		

		if int(self.char)<=3:

			self.ycord=0

		elif int(self.char)<=6:

			self.ycord=1

		elif int(self.char)<=9:

			self.ycord=2



	def erase_board(self):	

		for i in range(9):

			for j in range(9):

				if self.num_list[j][i]!=0:

					self.frame.delete(self.num_list[j][i])

				elif self.text_box[i][j]!=0:

					self.frame.delete(self.text_box[i][j])

				for k in range(3):			

					for l in range(3):			

						if self.note_list[i][j][k][l]!=0:			

							self.frame.delete(self.note_list[i][j][k][l])

		self.num_list = [[0]*9 for i in range(9)]





	def display_sudoku(self):

		self.entry_box = [[0]*9 for i in range(9)]

		self.text_box = [[0]*9 for i in range(9)]

		for i in range(9):

			for j in range(9):

				if self.board_print[i][j]==0:

					pass

				else:

					self.text = self.frame.create_text(76+51*j, 76+51*i, font=('AmericanTypewriter',20), text=self.board_print[i][j],anchor=CENTER)

					self.text_box[i][j]=self.text





	def change_easy(self):

		self.dif_button.config(text=self.a)

		self.e = self.a

		self.erase_board()

		easy_board = Board(self)

		easy_board_print = easy_board.generate('easy')

		self.board_print = easy_board_print

		self.board_copy = copy.deepcopy(self.board_print)

		self.entered_list = [[0 for x in range(9)] for x in range(9)]

		self.display_sudoku()

		self.delete_solution()

		for x in range(9):

			for y in range(9):

				self.frame.itemconfig(self.tiles[9*x+y],fill="white")

				self.tile_states[9*x+y] = False



		# for x in range(9):

		# 	print(*self.board_print[x])



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







	def new_game(self):

		print(self.e)

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



	def trace_mouse(self, event):

		# self.itemconfig(self.tiles[loc],fill="white" if self.tile_states[loc] else DBLUECOLOR)

		# 	self.tile_states[loc]=not self.tile_states[loc]

		# 	self.update()



		self.x, self.y = event.x, event.y

		self.cord = []

		for c in range(1,10):

			for d in range(1,10):

				if self.x >= 50+51*(c-1) and self.x <= 50+51*c and self.y >= 50+51*(d-1) and self.y <= 50+51*d:

					# print(c,d)

					# print(tile_states)

					for x in range(9):

						for y in range(9):

							if 9*x + y != 9*(c-1)+(d-1):

								self.frame.itemconfig(self.tiles[9*x+y],fill="white")

								self.tile_states[9*x+y] = False



					self.frame.itemconfig(self.tiles[9*(c-1)+(d-1)],fill="white" if self.board_print[d-1][c-1] != 0 or self.tile_states[9*(c-1)+(d-1)] else DBLUECOLOR)

					self.tile_states[9*(c-1)+(d-1)]	= not self.tile_states[9*(c-1)+(d-1)]

					# print(self.tile_states)

					self.frame.update()

					self.cord.append(c-1)

					self.cord.append(d-1)

					

					if self.tile_states[9*(c-1)+(d-1)]:

						self.pressed = True

					else:

						self.pressed = False

		

		if len(self.cord)!=0:

			self.cord_copy = self.cord

					



	def trace_keyboard(self, event):

		self.char = str(event.char)

		chars = ["1", "2", "3","4", "5", "6","7", "8", "9",]

		if self.char in chars:

			# print(self.var.get())

			if len(self.cord)!=0 and self.pressed == True and self.board_print[self.cord[1]][self.cord[0]] == 0 and self.var.get()==0:

				if self.num_list[self.cord[0]][self.cord[1]] == 0:

					for i in range(3):

						for j in range(3):					

							if self.note_list[self.cord[0]][self.cord[1]][i][j]!=0:						

								self.frame.delete(self.note_list[self.cord[0]][self.cord[1]][i][j])						

								self.note_list[self.cord[0]][self.cord[1]][i][j]=0

					

					self.enter_number = self.frame.create_text(76+51*(self.cord[0]), 76+51*(self.cord[1]), font=('Chalkduster',20), text=self.char, fill=FONTCOLOR)

					self.frame.itemconfig(self.tiles[9*self.cord[0]+self.cord[1]],fill="white")

					self.tile_states[9*self.cord[0]+self.cord[1]] = False



					# print(self.tiles[9*(self.cord[0]-1)+(self.cord[1]-1)])

					self.num_list[self.cord[0]][self.cord[1]] = self.enter_number

					self.entered_list[self.cord[1]][self.cord[0]] = int(self.char)

					self.pressed = False





				elif self.num_list[self.cord[0]][self.cord[1]]!=0:

					self.frame.delete(self.num_list[self.cord[0]][self.cord[1]])

					self.enter_number = self.frame.create_text(76+51*(self.cord[0]), 76+51*(self.cord[1]), font=('Chalkduster',20), text=self.char, fill=FONTCOLOR)

					self.frame.itemconfig(self.tiles[9*self.cord[0]+self.cord[1]],fill="white")

					self.tile_states[9*self.cord[0]+self.cord[1]] = False



					# print(self.tiles[9*self.cord[0]+self.cord[1]])



					self.num_list[self.cord[0]][self.cord[1]] = self.enter_number

					self.entered_list[self.cord[1]][self.cord[0]] = int(self.char)



					self.pressed = False



			elif self.board_print[self.cord_copy[1]][self.cord_copy[0]] == 0 and self.var.get()==1:

				self.x_y_location()

				if self.num_list[self.cord_copy[0]][self.cord_copy[1]] == 0 and self.note_list[self.cord_copy[0]][self.cord_copy[1]][self.xcord][self.ycord]==0:			 	

			 		self.enter_note = self.frame.create_text(76+51*(self.cord_copy[0])+51/3*(self.xcord-1), 76+51*(self.cord_copy[1])+51/3*(self.ycord-1), font=('Chalkduster',10), text=self.char, fill=FONTCOLOR)			 	

			 		self.note_list[self.cord_copy[0]][self.cord_copy[1]][self.xcord][self.ycord] = self.enter_note			 	

			 		self.frame.itemconfig(self.tiles[9*self.cord_copy[0]+self.cord_copy[1]],fill="white")			 	

			 		self.tile_states[9*self.cord_copy[0]+self.cord_copy[1]] = False

			 		self.pressed = False



				elif self.num_list[self.cord_copy[0]][self.cord_copy[1]] == 0 and self.note_list[self.cord_copy[0]][self.cord_copy[1]][self.xcord][self.ycord]!=0:			

					self.frame.delete(self.note_list[self.cord_copy[0]][self.cord_copy[1]][self.xcord][self.ycord])				

					self.note_list[self.cord_copy[0]][self.cord_copy[1]][self.xcord][self.ycord]=0

					self.pressed = False

			

			self.note_list_copy = self.note_list



	def trace_delete(self, event):

		# print(self.cord[0],self.cord[1])



		if self.pressed==True and self.board_print[self.cord[1]][self.cord[0]] == 0:

			if self.num_list[self.cord[0]][self.cord[1]]!=0:

				self.frame.delete(self.num_list[self.cord[0]][self.cord[1]])

				self.num_list[self.cord[0]][self.cord[1]]=0

				self.entered_list[self.cord[1]][self.cord[0]] = 0

				self.frame.itemconfig(self.tiles[9*self.cord[0]+self.cord[1]],fill="white")

				self.tile_states[9*self.cord[0]+self.cord[1]] = False

				self.pressed = False

			else:

				for x in range(3):

					for y in range(3):		

						# print(self.note_list_copy[self.cord[1]][self.cord[0]][x][y])

						if len(self.note_list_copy)!=0:

							self.frame.delete(self.note_list_copy[self.cord[1]][self.cord[0]][x][y])

							self.note_list_copy[self.cord[1]][self.cord[0]][x][y] = 0

						# print(self.note_list_copy[self.cord[1]][self.cord[0]][x][y])



	def check(self):

		check_board = Sudoku(self.board_print, self)

		# print(self.entered_list)

		wrong_entries, wrong_entry_box, wrong_entry_row, wrong_entry_column = check_board.wrong_entry(self.entered_list)

		if len(wrong_entries)==0:
			text = self.frame.create_text(600,200, font=('AmericanTypewriter',15), text="YOU ARE DOING WELL!", fill=FONTCOLOR, anchor=CENTER)
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

				# print(tile_num)

				self.frame.itemconfig(self.tiles[tile_num],fill=LREDCOLOR)



		for x in range(len(wrong_entries)):

			tile_num = 9*wrong_entries[x][1] + wrong_entries[x][0]

			self.frame.itemconfig(self.tiles[tile_num],fill=DREDCOLOR)





		# print(wrong_entry_box)



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



					# print('hi')

					text_print = self.frame.create_text(76+51*j, 76+51*i, font=('Chalkduster',20), text=self.board_print[i][j],anchor=CENTER,fill=FONTCOLOR)

					self.text_print_box[i][j]=text_print

					self.frame.update_idletasks()

					self.frame.after(1)

					# sudoku.frame.create_text

					sol=self.show_solution()

					if not sol:

						self.board_print[i][j] = 0

						self.frame.delete(self.text_print_box[i][j])

						# self.display.frame.update_idletasks()

						# self.display.frame.after(1)



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

			self.board_print = self.board_copy







def main():

	root = Tk()

	sudoku = Display(root)

	root.bind("<Key>", sudoku.trace_keyboard)	

	root.bind("<Button-1>", sudoku.trace_mouse)

	root.bind("<BackSpace>", sudoku.trace_delete)

	# sudoku.draw_rectangle()

	sudoku.draw_vertlines()

	sudoku.draw_horilines()

	sudoku.show_numbers()

	sudoku.show_letters()

	sudoku.display_sudoku()



	root.mainloop() 







main()