# https://www.youtube.com/watch?v=uqJZWLlnSqs&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=12

from tkinter import *
# > pip install pillow
# > pip freeze # see the package we installed
from PIL import ImageTk, Image
root = Tk()
root.title ("Radio Button")
root.iconbitmap('./pythonlogo_12x12.bmp')

Modes = [
    ("Pepperoni", "P"),
    ("Cheese", "C"),
    ("Mushroom", "M"),
    ("Onion", "O"),
]
# r = IntVar()
# r.set("2")   # set the the second option
pizza = StringVar()
pizza.set("Pepperoni")

for t, mode in Modes:
    print('t:', t)
    print('mode:', mode)
    Radiobutton (root, text=t, variable=pizza, value = mode, command=lambda: clicked(pizza.get())).pack(anchor=W)

def clicked (value):
    print('value:', value)
    myLabel = Label(root, text=value)
    myLabel.pack()

myLabel = Label(root, text=pizza.get())
myLabel.pack()

myButton = Button(root, text="Button Click", command=lambda: clicked (pizza.get()))
myButton.pack()

root.mainloop()