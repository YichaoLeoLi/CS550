from tkinter import *
import string

class Sudoku:

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


	def change_easy(self):
		self.dif_button.config(text=self.a)

	def change_intermediate(self):
		self.dif_button.config(text=self.b)

	def change_hard(self):
		self.dif_button.config(text=self.c)

	def change_evil(self):
		self.dif_button.config(text=self.d)

	def display_sudoku(self):
		for i in range(9):
			for j in range(9):
				if self.sudoku1[i][j]==0:
					self.e = Entry(frame,borderwidth=0)
					self.e.place(x=75.75+51.5*j,y=75.75+51.5*i,anchor=CENTER, width=30)
				else:
					frame.create_text(75.75+51.5*j, 75.75+51.5*i, font=('helvetica',20), text=self.sudoku1[i][j],anchor=CENTER)



root = Tk()


def main():

	sudoku = Sudoku(root)
	sudoku.draw_rectangle()
	sudoku.draw_vertlines()
	sudoku.draw_horilines()
	sudoku.show_numbers()
	sudoku.show_letters()
	sudoku.display_sudoku()

	root.mainloop()





main()