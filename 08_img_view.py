# https://www.youtube.com/watch?v=NoTM8JciWaQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=8

from tkinter import *
# > pip install pillow
# > pip freeze # see the package we installed
from PIL import ImageTk, Image
root = Tk()
root.title ("Image Viewer and Exit Button")
root.iconbitmap('./pythonlogo_12x12.bmp')

my_img = ImageTk.PhotoImage (Image.open ('./pythonlogo.png'))
my_label = Label (image=my_img)
my_label.pack()

button_quit = Button (root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()