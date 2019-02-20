from tkinter import *
import string

class Display:

	def __init__(self, master):
		global frame
		frame = Canvas(master, width = 700, height = 600)
		frame.pack()
		self.a = "easy"
		self.b = "intermediate"
		self.c = "hard"
		self.d = "evil"
		self.e = 0
		self.dif_button = Menubutton(frame, text="easy", width = 10)
		self.dif_button.menu = Menu(self.dif_button)
		self.dif_button["menu"] = self.dif_button.menu
		self.dif_button.menu.add_command(label=self.a, command=self.change_easy)
		self.dif_button.menu.add_command(label=self.b, command=self.change_intermediate)
		self.dif_button.menu.add_command(label=self.c, command=self.change_hard)
		self.dif_button.menu.add_command(label=self.d, command=self.change_evil)
		self.dif_button.place(x=600, y=400, anchor=CENTER)

		self.new_game_button = Button(frame, text="new game", width=13)
		self.new_game_button.place(x=600,y=350,anchor=CENTER)

		self.show_solution_but = Button(frame, text="show solution", width=13)
		self.show_solution_but.place(x=600, y=550,anchor=CENTER)

		self.note_button = Checkbutton(frame, text="note")
		self.note_button.place(x=400, y=550,anchor=CENTER)


		self.sudoku1 = [[0,0,3,0,2,0,6,0,0],[9,0,0,3,0,5,0,0,1],[0,0,1,8,0,6,4,0,0],[0,0,8,1,0,2,9,0,0],[7,0,0,0,0,0,0,0,8],[0,0,6,7,0,8,2,0,0],[0,0,2,6,0,9,5,0,0],[8,0,0,2,0,3,0,0,9],[0,0,5,0,1,0,3,0,0]]
		self.sudoku2 = [[0,4,5,0,0,0,0,0,0],[8,3,0,0,0,7,4,0,0],[0,0,0,2,0,0,0,5,0],[0,8,4,6,0,0,5,0,1],[2,0,0,8,3,0,0,4,0],[0,0,0,5,0,0,0,0,7],[3,7,0,0,0,5,0,6,0],[0,2,0,0,0,0,0,8,0],[5,6,1,9,0,0,0,7,0]]
		self.board_print = self.sudoku1
	
		self.x = 0
		self.y = 0
		self.char = 0
		self.pressed=False
		self.enter_number=0
		self.num_list=[[0]*9 for i in range(9)]
 
	def draw_rectangle(self):
		frame.create_rectangle(50, 50, 512, 512, width = 2)

	def draw_vertlines(self):
		for i in range(1, 9):
			if i != 3 and i != 6:
				frame.create_line(50+i*51.5,50,50+i*51.5,512)
			else:
				frame.create_line(50+i*51.5,50,50+i*51.5,512,width=2)

	def draw_horilines(self):
		for i in range(1,9):
			if i != 3 and i != 6:
				frame.create_line(50, 50+i*51.5, 512, 50+i*51.5)
			else:
				frame.create_line(50, 50+i*51.5, 512, 50+i*51.5,width=2)
	
	def show_numbers(self):
		for i in range(1,10):
			frame.create_text(75.75+51.5*(i-1), 30, text=i)

	def show_letters(self):
		for i in range(1,10):
			frame.create_text(30, 75.75+51.5*(i-1), text=string.ascii_uppercase[i-1])

	def erase_board(self):	
		for i in range(9):
			for j in range(9):
				if self.num_list[j][i]!=0:
					frame.delete(self.num_list[j][i])
				elif self.text_box[i][j]!=0:
					frame.delete(self.text_box[i][j])
		self.num_list = [[0]*9 for i in range(9)]

	def display_sudoku(self):
		self.entry_box = [[0]*9 for i in range(9)]
		self.text_box = [[0]*9 for i in range(9)]
		for i in range(9):
			for j in range(9):
				if self.board_print[i][j]==0:
					# self.e = Entry(frame,borderwidth=0,justify=CENTER,font=('helvetica',20),textvariable=self.numberr)
					# self.entry_box[i][j]=self.e
					# self.e.place(x=75.75+51.5*j,y=75.75+51.5*i,anchor=CENTER, width=30)
					pass
				else:
					self.text = frame.create_text(75.75+51.5*j, 75.75+51.5*i, font=('helvetica',20), text=self.board_print[i][j],anchor=CENTER)
					self.text_box[i][j]=self.text


	def change_easy(self):
		self.dif_button.config(text=self.a)
		self.erase_board()
		self.board_print = self.sudoku1
		self.display_sudoku()

	def change_intermediate(self):
		self.dif_button.config(text=self.b)
		self.erase_board()
		self.board_print = self.sudoku2
		self.display_sudoku()

	def change_hard(self):
		self.dif_button.config(text=self.c)

	def change_evil(self):
		self.dif_button.config(text=self.d)



	def trace_mouse(self, event):
		self.x, self.y = event.x, event.y
		self.cord = []
		for c in range(1,10):
			for d in range(1,10):
				if self.x >=50+51.3*(c-1) and self.x<=101.3+51.3*(c-1) and self.y>=50+51.3*(d-1) and self.y<=101.3+51.3*(d-1):
					print(c,d)
					self.cord.append(c)
					self.cord.append(d)
					self.pressed=True
					

		#print(self.x, self.y)

	def trace_keyboard(self, event):
		#print("pressed", str(event.char))
		self.char = str(event.char)
		#print(self.board_print[self.cord[1]-1][self.cord[0]-1])
		if self.char == "1" or self.char == "2" or self.char == "3" or self.char == "4" or self.char == "5" or self.char == "6" or self.char == "7" or self.char == "8" or self.char == "9":
			if self.pressed==True and self.board_print[self.cord[1]-1][self.cord[0]-1] == 0:
				if self.num_list[self.cord[0]-1][self.cord[1]-1]==0:
					self.enter_number = frame.create_text(75.75+51.5*(self.cord[0]-1), 75.75+51.5*(self.cord[1]-1), font=('helvetica',20), text=self.char)
					self.num_list[self.cord[0]-1][self.cord[1]-1] = self.enter_number
				elif self.num_list[self.cord[0]-1][self.cord[1]-1]!=0:
					frame.delete(self.num_list[self.cord[0]-1][self.cord[1]-1])
					self.enter_number = frame.create_text(75.75+51.5*(self.cord[0]-1), 75.75+51.5*(self.cord[1]-1), font=('helvetica',20), text=self.char)
					self.num_list[self.cord[0]-1][self.cord[1]-1] = self.enter_number
	def trace_delete(self, event):
		 if self.pressed==True and self.board_print[self.cord[1]-1][self.cord[0]-1] == 0:
		 	if self.num_list[self.cord[0]-1][self.cord[1]-1]!=0:
		 		frame.delete(self.num_list[self.cord[0]-1][self.cord[1]-1])
		 		self.num_list[self.cord[0]-1][self.cord[1]-1]=0
			








def main():
	root = Tk()
	sudoku = Display(root)
	#root.bind("<Motion>", sudoku.trace_mouse)
	root.bind("<Key>", sudoku.trace_keyboard)	
	root.bind("<Button-1>", sudoku.trace_mouse)
	root.bind("<BackSpace>", sudoku.trace_delete)
	sudoku.draw_rectangle()
	sudoku.draw_vertlines()
	sudoku.draw_horilines()
	sudoku.show_numbers()
	sudoku.show_letters()
	sudoku.display_sudoku()

	root.mainloop() 





main()