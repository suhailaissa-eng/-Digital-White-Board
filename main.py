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





root.mainloop()