# https://www.youtube.com/watch?v=S3AaSwpb5GE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=13

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog 

root = Tk()
root.title ("Root")
root.iconbitmap('./pythonlogo_12x12.bmp')

root.filename = filedialog.askopenfilename(initialdir="./images", \
    title="Select a file", \
    filetypes=(("jpg files", "*.jpg"),("png files", "*.png"),("all files", "*.*")))
my_label = Label(root, text=root.filename).pack()
my_image = ImageTk.PhotoImage(Image.open(root.filename))
my_image_label = Label(image=my_image).pack()

root.mainloop()