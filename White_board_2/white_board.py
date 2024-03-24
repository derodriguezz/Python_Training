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
Label(root, image=color_box, bg="#f2f3f5").place(x=10, y=15)

# eraser
eraser = PhotoImage(file="eraser.png"





# Mainscreen
canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)

# Dibuja un rectángulo con esquinas redondeadas
create_rounded_rectangle(canvas, 10, 10, 920, 490, radius=24, outline="#d7d7d7")

root.mainloop()
