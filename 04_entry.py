# https://www.youtube.com/watch?v=7A_csP9drJw&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=4

# We will position in TKinter's Grid system
from tkinter import *
root = Tk()

#e = Entry (root, width=50, bg='blue', fg='white', border=5)
e = Entry (root, width=50)
e.pack()
e.insert(0, "Insert Your name")

def myClick ():
    # myLabel = Label (root, text="Look! I Clicked a Button!!")
    # Get the name from e = Entry ()
    hello = "Hello " +e.get()
    myLabel = Label (root, text= hello)
    myLabel.pack()

myButton = Button (root, text="Enter your name", command=myClick)
myButton.pack()


root.mainloop()