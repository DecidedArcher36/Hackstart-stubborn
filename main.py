import tkinter as tk

from tkinter import *

# opens a window
root=tk.Tk()
# sets size of the window
root.geometry('1920x1080')

pressed = False


text_box= None

def get_text():
    # Retrieve the text currently typed into the text box
    user_input = text_box.get()
    
    if user_input == "5n5ym":
        result_label.config(text="You have entered the correct code")
    else:
        result_label.config(text="You have entered the incorrect code")


def showtext():
    result_label.config(text="You have passed, you did not click on the captcha tick box")
    
    text_box = tk.Entry(root, width=30, font=("Arial", 12))
    text_box.pack()
    pressed = True
    captcha_image.config(image=textImage, bg="lightgreen")
    level_Label.config(text="Level 2")

    text_box = tk.Entry(root, width=30, font=("Arial", 12))
    text_box.pack()
    level1Result = False
    level2Result = True

    if pressed == True:
         # Retrieve the text currently typed into the text box
        user_input = text_box.get()
            
        if user_input == "5n5ym":
            result_label.config(text="You have entered the correct code")
        else:
            result_label.config(text="You have entered the incorrect code")
    



def on_image_click(event):
    result_label.config(text="Failed, you were not meant to click on the tick box to pass")
    level1Result = False

level_Label = tk.Label(root,text="Level 1")
level_Label.pack()


image = PhotoImage(file="captcha.png")

textImage = PhotoImage(file="text.png")
captcha_image = tk.Label(root, image=image)
captcha_image.pack()

captcha_image.bind("<Button-1>", on_image_click)
#trying to make text appear when button is pressed
button = tk.Button(root,width=50,height=15, text="verify",command=showtext)

button.pack()


result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

label = tk.Label(root)
label.pack()

root.mainloop()




