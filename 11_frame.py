# https://www.youtube.com/watch?v=_auZ8TTkojQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=11

from tkinter import *
# > pip install pillow
# > pip freeze # see the package we installed
from PIL import ImageTk, Image
root = Tk()
root.title ("Frame")
root.iconbitmap('./pythonlogo_12x12.bmp')

frame = LabelFrame (root, text="This is my Frame", padx=70, pady=70)
frame.pack(padx=10, pady=10)

b1 = Button (frame, text="Click Here 1", padx=10, pady=10)
b2 = Button (frame, text="Click Here 2", padx=10, pady=10)
# b.pack(padx=20, pady=10)
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)
root.mainloop()