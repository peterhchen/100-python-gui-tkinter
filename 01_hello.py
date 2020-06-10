# python tkinter is a GUI tool from TCL/TK.
from tkinter import *

# TK always start with a root.
root = Tk()
# create a label widget
myLabel = Label(root, text="Hello World!")
# Put the widget in the window
# shoving it onto the screen.
myLabel.pack()

# last thing we do is to create an event loop.
# WHen you have a GUI running, it loops for mouse, 
# click button, It is a constant loop.
root.mainloop()
# to execute it
# Python 01_hello.py
# You can resize and click the blank area to move the window.