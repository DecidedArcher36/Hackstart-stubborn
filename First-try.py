<<<<<<< HEAD

import tkinter as tk
from tkinter import *

# opens a window
root=tk.Tk()
# sets size of the window
root.geometry('800x1200')


image = PhotoImage(file="Smile.png")
image_label = tk.Label(root, image=image)
image_label.pack()

#trying to make text appear when button is pressed
button = tk.Button(root, text="Click", command=lambda: label.config(text="Hello")).pack(())

label = tk.Label(root)
label.pack()

root.mainloop()
=======

import tkinter as tk
from tkinter import *

print("Hello World")

# opens a window
root=tk.Tk()
# sets size of the window
root.geometry('800x1200')

def makeimage():
    #trying to show an image on screen
    image = PhotoImage(file="smile.png")
    image_label = tk.Label(root, image)
    image_label.pack()


makeimage()

#trying to make text appear when button is pressed
button = tk.Button(root, text="Click", command=lambda: label.config(text="Hello")).pack(())
button.pack()
label = tk.Label(root)
label.pack()




root.mainloop()

>>>>>>> c2949351cf49e7a8fd3f4d0bff994f6e72781833
