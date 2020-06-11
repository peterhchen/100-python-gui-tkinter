# https://www.youtube.com/watch?v=zg4c92pNFeo&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=9

from tkinter import *
# > pip install pillow
# > pip freeze # see the package we installed
from PIL import ImageTk, Image
root = Tk()
root.title ("Image Viewer and Exit Button")
root.iconbitmap('./pythonlogo_12x12.bmp')

my_img0 = ImageTk.PhotoImage (Image.open ('./images/dog0.jpg'))
my_img1 = ImageTk.PhotoImage (Image.open ('./images/dog1.jpg'))
my_img2 = ImageTk.PhotoImage (Image.open ('./images/dog2.jpg'))
my_img3 = ImageTk.PhotoImage (Image.open ('./images/dog3.jpg'))
my_img4 = ImageTk.PhotoImage (Image.open ('./images/dog4.jpg'))
image_list = [my_img0, my_img1, my_img2, my_img3, my_img4]
my_label = Label (image=my_img0)        # default is image[0] = dog1.jpg
my_label.grid(row=0, column=0, columnspan=3)    # Put on the screen

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    print('forward => image_number:', image_number)
    my_label = Label (image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    if image_number == 5:
        print('state=DISABLED')
        button_forward = Button(root, text=">>", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    print('back => image_number:', image_number)
    my_label = Label (image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    if image_number == 1:
        print('state=DISABLED')
        button_back = Button(root, text="<<", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_quit = Button (root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(1))
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()