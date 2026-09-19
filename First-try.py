
import tkinter as tk
from tkinter import *

# opens a window
root=tk.Tk()
# sets size of the window
root.geometry('1920x1080')


image = PhotoImage(file="Smile.png")
image_label = tk.Label(root, image=image)
image_label.pack()

#trying to make text appear when button is pressed
button = tk.Button(root, text="Click", command=lambda: label.config(text="Hello")).pack(())

label = tk.Label(root)
label.pack()

root.mainloop()
