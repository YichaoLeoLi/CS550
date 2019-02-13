from tkinter import *


class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

        self.whatsup = Button(frame, text="???", command = self.whatsup)
        self.whatsup.pack()

    def say_hi(self):
        print ("hi there, everyone!")

    def whatsup(self):
    	print("??????")
    	quit()

root = Tk()

app = App(root)

root.mainloop()

create_line()
