# https://www.youtube.com/watch?v=F5PfbC5ld-Q&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=5

from tkinter import *
root = Tk()
root.title ("Simple Calculator")

e = Entry (root, width=35, borderwidth=5)
def button_click(number):
    # do not clear one digit.
    #e.delete(0, END)
    # right now the number insert from the front.
    # it is reverse.
    e.insert(0, number)
    return

e.grid(row=0, column=0, columnspan=3, padx=20, pady=20) # the text input span 3 columns

# Define button
# Lambda let you pass the parameter
#button_1=Button(root, text="1", padx=40, pady=20, command=button_click)
button_1=Button(root, text="1", padx=40, pady=20, command=lambda:button_click(1))
button_2=Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3=Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4=Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5=Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6=Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7=Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8=Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9=Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0=Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add=Button(root, text="+", padx=40, pady=20, command=lambda: button_click())
button_equal=Button(root, text="=", padx=87, pady=20, command=lambda: button_click())
button_clear=Button(root, text="Clear", padx=77, pady=20, command=lambda: button_click())

#set button on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2) # span two columns
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2) # span two columns
root.mainloop()