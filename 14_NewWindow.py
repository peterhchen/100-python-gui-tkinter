# https://www.youtube.com/watch?v=S3AaSwpb5GE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=13

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title ("Root")
root.iconbitmap('./pythonlogo_12x12.bmp')

def open():
    global my_image     # only global image can be popup by root.
    top = Toplevel()
    top.title ("Second Window")
    top.iconbitmap('./pythonlogo_12x12.bmp')
    my_image = ImageTk.PhotoImage(Image.open("images/dog1.jpg"))
    my_lbl = Label (top, image=my_image).pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()

btn= Button(root, text="Open Second Window", command=open).pack()

# How to add different kinds of window?
# top = Toplevel()
# top.title ("Second Window")
# top.iconbitmap('./pythonlogo_12x12.bmp')
# my_image = ImageTk.PhotoImage(Image.open("images/dog1.jpg"))
# my_lbl = Label (top, image=my_image).pack()


root.mainloop()