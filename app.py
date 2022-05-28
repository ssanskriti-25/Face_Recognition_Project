import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile
import os

root = tk.Tk()
canvas = tk.Canvas(root,width=1000, height=150)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('1.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1 , row=0)

def main():
  os.system('main.py')
  
#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:main(), font="Raleway", bg="#20bebe" , fg="black" , height=2, width=20, justify="center")
browse_text.set("Take Attendance")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root,width=20, height=25)
canvas.grid(columnspan=3)
root.mainloop()
