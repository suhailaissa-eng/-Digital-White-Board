from tkinter import * 
from tkinter.colorchooser import askcolor 
from tkinter import ttk 
import tkinter as tk 
from tkinter import filedialog 
import os 

root = Tk() 
root.title("WHITE BOARD") 
root.geometry("1050x570+150+50") 
root.config(bg="#f2f3f5") 
root.resizable(False, False)

current_x= 0
current_y = 0
color = "black"

def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y

def addline(work):
    global current_x, current_y
    canvas.create_line((current_x, current_y, work.x, work.y), 
                       width=get_current_value(), fill=color, 
                       capstyle=ROUND, smooth=True)
    current_x, current_y = work.x, work.y

def show_color(new_color):
    global color
    color = new_color

def new_canvas():
    canvas.delete('all')
    display_palette()

def insertimage():
    global filename
    global f_img
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file",
                                          filetypes=[("PNG file", "*.png"), ("All files", "new.txt")])
    
    f_img = tk.PhotoImage(file=filename)
    my_img=canvas.create_image(180, 50, image=f_img)
    root.bind("<B3-Motion>",my_callback)

def use_eraser():
    global color
    color = "white"


def my_callback(event):
    global f_img

   
    f_img = tk.PhotoImage(file=filename)
    my_img=canvas.create_image(event.x, event.y, image=f_img, anchor="nw")

root.bind("<B3-Motion>", my_callback)

image_icon = PhotoImage(file="images/logo.png")
root.iconphoto(False, image_icon)


color_box = PhotoImage(file="images/colorsection.png")
Button(root, image=color_box, bg="#f2f3f5", command=new_canvas, borderwidth=0).place(x=10, y=20)


eraser = PhotoImage(file="images/eraser.png")
Button(root, image=eraser, bg="#f2f3f5", command=use_eraser).place(x=30, y=400)


importimage = PhotoImage(file="images/addimage.png")
Button(root, image=importimage, bg="white", command=insertimage).place(x=30, y=450)


colors = Canvas(root, bg="#fff", width=37, height=300, bd=0)
colors.place(x=30, y=60)


canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)

canvas.bind('<Button-1>', locate_xy) 
canvas.bind('<B1-Motion>', addline)

current_color = "black"




def display_palette():
    color_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "gray"]
    y_position = 10

    for color in color_list:
        id = colors.create_rectangle(10, y_position, 30, y_position + 20, fill=color)
        colors.tag_bind(id, '<Button-1>', lambda x, c=color: show_color(c))
        y_position += 30

display_palette()


current_value = tk.DoubleVar()

def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=slider_changed, variable=current_value)
slider.place(x=30, y=530)

value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27, y=550)



root.mainloop()
