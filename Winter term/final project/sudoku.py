from tkinter import *
import string

class Sudoku:

	def __init__(self, master):
		global frame
		frame = Canvas(master, width = 700, height = 600)
		frame.pack()
		
		self.dif_button = Menubutton(frame, text="Easy", width = 10, height=10)
		self.dif_button.place(x=600, y=500, anchor=CENTER)

 
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


root = Tk()


def main():

	sudoku = Sudoku(root)
	sudoku.draw_rectangle()
	sudoku.draw_vertlines()
	sudoku.draw_horilines()
	sudoku.show_numbers()
	sudoku.show_letters()

	root.mainloop()





main()