# https://www.youtube.com/watch?v=uqJZWLlnSqs&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=12

from tkinter import *
# > pip install pillow
# > pip freeze # see the package we installed
from PIL import ImageTk, Image
root = Tk()
root.title ("Radio Button")
root.iconbitmap('./pythonlogo_12x12.bmp')

r = IntVar()
r.set("2")   # set the the second option
def clicked (value):
    print('value:', value)
    myLabel = Label(root, text=value)
    myLabel.pack()

# r = StrVar()
# r.get()   # to get the option of radio button
# tkinter have their own variable which is different from Python variable.
Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
myLabel = Label(root, text=r.get())
myLabel.pack()

myButton = Button(root, text="Buuton Click", command=lambda: clicked (r.get()))
myButton.pack()

root.mainloop()