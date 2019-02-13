from tkinter import *


root = Tk()


pane = Frame(root)
Label(pane, text="Pane Title").pack()
b = Button(pane, width=12, height=12, text="hi")
b.place(relx=1, x=2, y=2, anchor=NE)


root.mainloop()

