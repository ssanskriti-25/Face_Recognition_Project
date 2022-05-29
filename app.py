import tkinter as tk                           #Importing the necessary libraries
from tkinter import filedialog
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile
import os

root = tk.Tk()            #Beginning of the interface
canvas = tk.Canvas(root,width=1000, height=150)                       #To set the size of the canvas
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('1.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1 , row=0)

# Defination of the main function is done
def main():
  os.system('main.py')
  
#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:main(), font="Raleway", bg="#20bebe" , fg="black" , height=2, width=20, justify="center")
browse_text.set("Take Attendance")
browse_btn.grid(column=1, row=2)
canvas = tk.Canvas(root,width=20, height=25)
canvas.grid(columnspan=3)
root.mainloop()                              #End of the interface
