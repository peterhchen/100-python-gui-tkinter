# We will position in TKinter's Grid system
from tkinter import *
root = Tk()

myLabel1 = Label (root, text="Hello World!")
myLabel2 = Label (root, text="My Name is Peter Chen")
myLabel3 = Label (root, text="                      ")
# Instead of pack(), we use grid
myLabel1.grid(row=0, column=0)
# Even we put column 5. It still look like 1.
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)
root.mainloop()