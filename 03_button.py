# We will position in TKinter's Grid system
from tkinter import *
root = Tk()
def myClick ():
    myLabel = Label (root, text="Look! I Clicked a Button!!")
    myLabel.pack()

#myButton = Button (root, text="Click Me!", state=DISABLED)
# myButton = Button (root, text="Click Me!", padx=5, pady=10)
# Create a callback by command=callback
# do not add paranethesis to function call myCLick()
#myButton = Button (root, text="Click Me!", command=myClick())
myButton = Button (root, text="Click Me!", command=myClick, fg="blue", bg="red")
myButton.pack()


root.mainloop()