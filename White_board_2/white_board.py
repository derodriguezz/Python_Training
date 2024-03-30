from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import os

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    """Crea un rectángulo con esquinas redondeadas en el canvas dado."""
    # Dibuja las esquinas redondeadas
    canvas.create_arc(x1, y1, x1 + radius * 2, y1 + radius * 2, start=90, extent=90, style=ARC, **kwargs)
    canvas.create_arc(x2 - radius * 2, y1, x2, y1 + radius * 2, start=0, extent=90, style=ARC, **kwargs)
    canvas.create_arc(x2 - radius * 2, y2 - radius * 2, x2, y2, start=270, extent=90, style=ARC, **kwargs)
    canvas.create_arc(x1, y2 - radius * 2, x1 + radius * 2, y2, start=180, extent=90, style=ARC, **kwargs)
    # Dibuja los lados rectos
    
    canvas.create_line(x1 + radius, y1, x2 - radius, y1, **kwargs)
    canvas.create_line(x1 + radius, y2, x2 - radius, y2, **kwargs)
    canvas.create_line(x1, y1 + radius, x1, y2 - radius, **kwargs)
    canvas.create_line(x2, y1 + radius, x2, y2 - radius, **kwargs)

root = tk.Tk()

root.title("WHITE BOARD")
root.geometry("1050x570+150+50")
root.config(bg="#f2f3f5")
root.resizable(False, False)

# Icon
image_icon = PhotoImage(file="pen_icon1.png")
root.iconphoto(False, image_icon)

# Sidebar
color_box = PhotoImage(file="bar_icon.png")
Label(root, image=color_box, bg="#f2f3f5").place(x=10, y=30)

# eraser
eraser = PhotoImage(file="eraser_icon.png")
Button(root, image = eraser, bg = "#f2f3f5").place(x=35,y=390)

# import image
importimage = PhotoImage(file="add_image.png")
Button(root, image = importimage, bg="white").place(x=35, y=430)


###color
colors = Canvas(root, bg = "#fff", width = 37, height = 300, bd=0)
colors.place(x=30, y=60)

def display_pallete():
    id= colors.create_rectangle((10,10,30,30,), fill= "black")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

    id= colors.create_rectangle((10,40,30,60,), fill= "white")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('white'))

    id= colors.create_rectangle((10,70,30,90,), fill= "gray")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))

    id= colors.create_rectangle((10,100,30,120,), fill= "brown")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown'))
    
    id= colors.create_rectangle((10,130,30,150,), fill= "red")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))

    id= colors.create_rectangle((10,160,30,180,), fill= "yellow")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))

    id= colors.create_rectangle((10,190,30,210,), fill= "green")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))

    id= colors.create_rectangle((10,220,30,240,), fill= "blue")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))

    id= colors.create_rectangle((10,250,30,270,), fill= "purple")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))

display_pallete()

# Mainscreen
canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)

# Dibuja un rectángulo con esquinas redondeadas
create_rounded_rectangle(canvas, 10, 10, 920, 490, radius=24, outline="#d7d7d7")

root.mainloop()
