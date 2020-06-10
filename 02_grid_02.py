# We will position in TKinter's Grid system
from tkinter import *
root = Tk()

# we can attached the cascade function call.
myLabel1 = Label (root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label (root, text="My Name is Peter Chen").grid(row=1, column=5)

root.mainloop()