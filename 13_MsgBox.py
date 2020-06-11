# https://www.youtube.com/watch?v=S3AaSwpb5GE&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=13

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title ("Popup")
root.iconbitmap('./pythonlogo_12x12.bmp')

# different kinds of message bixes:
# showinfo, showwarning, showerro, askquestion, askokcancel, askyesno
def popup():
    # Display title and content
    #messagebox.showinfo("This is my popup", "Hello World!")
    # messagebox.showwarning("This is my popup", "Hello World!")
    #messagebox.showerror("This is my popup", "Hello World!")
    # messagebox.askquestion("This is my popup", "Hello World!")
    #messagebox.askokcancel("This is my popup", "Hello World!")
    response = messagebox.askyesno("This is my popup", "Hello World!")
    Label(root, text="You clicked " + str(response)).pack()
    # display "1" or "0" or "Yes" or "No"
    # if response == 1:
    #     Label(root, text="You clicked Yes").pack()
    # else:
    #     Label(root, text="You clicked No").pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()