from tkinter import * 
from tkinter.colorchooser import askcolor 
from tkinter import ttk 
import tkinter as tk 
from tkinter import filedialog 
import os 
root=Tk() 
root.title("WHITE BOARD") 
root.geometry("1050x570+150+50") 
root.config(bg="#f2f3f5") 
root.resizable (False, False)



image_icon=PhotoImage(file="images/logo.png")
root.iconphoto(False,image_icon)



color_box = PhotoImage(file="images/colorsection.png")
Label(root, image=color_box, bg="#f2f3f5").place(x=10, y=20)

eraser = PhotoImage(file="images/eraser.png")
Button(root, image=eraser, bg="#f2f3f5").place(x=30, y=400)

import_image = PhotoImage(file="images/addimage.png")
Button(root, image=import_image, bg="white").place(x=30, y=450)


canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)





root.mainloop()