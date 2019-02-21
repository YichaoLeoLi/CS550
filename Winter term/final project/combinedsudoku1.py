from tkinter import *
import string

# Eric Li
# Feb 8, 2019

import random
import copy
import numpy as np

LBLUECOLOR = "#%02x%02x%02x" % (176,224,230) 	# https://stackoverflow.com/questions/41383849/setting-the-fill-of-a-rectangle-drawn-with-canvas-to-an-rgb-value
DBLUECOLOR = "#%02x%02x%02x" % (163,206,220)
FONTCOLOR  = "#%02x%02x%02x" % (106,90,205)

class Sudoku:
	def __init__(self, board):
		self.board = board

	def full(self):
		for i in range(9):
			for j in range(9):
				if self.board[i][j] == 0:
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

	def valid_entries(self, possible_entries):
		valid_entries = []
		possible_entries.pop(0)
		for x in range(9):
			if possible_entries[x] == 0:
				valid_entries.append(x+1)

		random.shuffle(valid_entries)
		return valid_entries

	def solve(self):
		# update_gui(self.board)
		if self.full():
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
			

class Board:
	def __init__(self):
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


		initial_board = Sudoku(self.init_board)
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
				board_test_1 = Sudoku(copy.deepcopy(board_new))
				board_solved_1 = board_test_1.solve()

				board_test_2 = Sudoku(copy.deepcopy(board_new))
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
		self.e = 0
		self.dif_button = Menubutton(self.frame, text="easy", width = 10)
		self.dif_button.menu = Menu(self.dif_button)
		self.dif_button["menu"] = self.dif_button.menu
		self.dif_button.menu.add_command(label=self.a, command=self.change_easy)
		self.dif_button.menu.add_command(label=self.b, command=self.change_intermediate)
		self.dif_button.menu.add_command(label=self.c, command=self.change_hard)
		self.dif_button.menu.add_command(label=self.d, command=self.change_evil)
		self.dif_button.place(x=600, y=400, anchor=CENTER)

		self.new_game_button = Button(self.frame, text="new game", width=13)
		self.new_game_button.place(x=600,y=350,anchor=CENTER)

		self.show_solution_but = Button(self.frame, text="show solution", width=13)
		self.show_solution_but.place(x=600, y=550,anchor=CENTER)

		self.note_button = Checkbutton(self.frame, text="note")
		self.note_button.place(x=400, y=550,anchor=CENTER)

		initial_board = Board()
		sudoku1 = initial_board.generate('easy')
		# self.sudoku1 = [[0,0,3,0,2,0,6,0,0],[9,0,0,3,0,5,0,0,1],[0,0,1,8,0,6,4,0,0],[0,0,8,1,0,2,9,0,0],[7,0,0,0,0,0,0,0,8],[0,0,6,7,0,8,2,0,0],[0,0,2,6,0,9,5,0,0],[8,0,0,2,0,3,0,0,9],[0,0,5,0,1,0,3,0,0]]
		self.board_print = sudoku1
	
		self.x = 0
		self.y = 0
		self.char = 0
		self.pressed=False
		self.enter_number=0
		self.num_list=[[0]*9 for i in range(9)]
 
	# def draw_rectangle(self,*args,loc=None,**kwargs):
	# 	self.tile_states[loc] = False  # All tiles are initially not activated
	# 	if loc and self.inputmode:
	# 		return super().create_rectangle(50, 50*args, **kwargs, tags=loc)
	# 	else:
	# 		return super().create_rectangle(*args, **kwargs)

	# def draw_rectangle(self):
	# 	frame.create_rectangle(50, 50, 512, 512, width = 2)

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

	def erase_board(self):	
		for i in range(9):
			for j in range(9):
				if self.num_list[j][i]!=0:
					self.frame.delete(self.num_list[j][i])
				elif self.text_box[i][j]!=0:
					self.frame.delete(self.text_box[i][j])

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
		self.erase_board()
		easy_board = Board()
		easy_board_print = easy_board.generate('easy')
		self.board_print = easy_board_print
		self.display_sudoku()

		for x in range(9):
			print(*self.board_print[x])

	def change_intermediate(self):
		self.dif_button.config(text=self.b)
		self.erase_board()
		intermediate_board = Board()
		intermediate_board_print = intermediate_board.generate('interdediate')
		self.board_print = intermediate_board_print
		self.display_sudoku()

	def change_hard(self):
		self.dif_button.config(text=self.c)
		self.erase_board()
		hard_board = Board()
		hard_board_print = hard_board.generate('hard')
		self.board_print = hard_board_print
		self.display_sudoku()

	def change_evil(self):
		self.dif_button.config(text=self.d)
		self.erase_board()
		evil_board = Board()
		evil_board_print = evil_board.generate('evil')
		self.board_print = evil_board_print
		self.display_sudoku()


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
							self.frame.itemconfig(self.tiles[9*x+y],fill="white")
							self.tile_states[9*x+y] = False

					self.frame.itemconfig(self.tiles[9*(c-1)+(d-1)],fill="white" if self.board_print[d-1][c-1] != 0 or self.tile_states[9*(c-1)+(d-1)] else DBLUECOLOR)
					self.tile_states[9*(c-1)+(d-1)]	= not self.tile_states[9*(c-1)+(d-1)]
					# print(tile_states)
					self.frame.update()
					self.cord.append(c-1)
					self.cord.append(d-1)
					self.pressed=True
					
	def trace_keyboard(self, event):
		self.char = str(event.char)
		chars = ["1", "2", "3","4", "5", "6","7", "8", "9",]
		if self.char in chars:
			if self.pressed == True and self.board_print[self.cord[1]][self.cord[0]] == 0:
				if self.num_list[self.cord[0]][self.cord[1]] == 0:
					self.enter_number = self.frame.create_text(76+51*(self.cord[0]), 76+51*(self.cord[1]), font=('Chalkduster',20), text=self.char, fill=FONTCOLOR)
					self.frame.itemconfig(self.tiles[9*self.cord[0]+self.cord[1]],fill="white")
					self.tile_states[9*self.cord[0]+self.cord[1]] = False

					# print(self.tiles[9*(self.cord[0]-1)+(self.cord[1]-1)])
					self.num_list[self.cord[0]][self.cord[1]] = self.enter_number

				elif self.num_list[self.cord[0]][self.cord[1]]!=0:
					self.frame.delete(self.num_list[self.cord[0]][self.cord[1]])
					self.enter_number = self.frame.create_text(76+51*(self.cord[0]), 76+51*(self.cord[1]), font=('Chalkduster',20), text=self.char, fill=FONTCOLOR)
					self.frame.itemconfig(self.tiles[9*self.cord[0]+self.cord[1]],fill="white")
					self.tile_states[9*self.cord[0]+self.cord[1]] = False

					# print(self.tiles[9*self.cord[0]+self.cord[1]])

					self.num_list[self.cord[0]][self.cord[1]] = self.enter_number

	def trace_delete(self, event):
		 if self.pressed==True and self.board_print[self.cord[1]][self.cord[0]] == 0:
		 	if self.num_list[self.cord[0]][self.cord[1]]!=0:
		 		self.frame.delete(self.num_list[self.cord[0]][self.cord[1]])
		 		self.num_list[self.cord[0]][self.cord[1]]=0
		 		self.frame.itemconfig(self.tiles[9*self.cord[0]+self.cord[1]],fill="white")
		 		self.tile_states[9*self.cord[0]+self.cord[1]] = False

			








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