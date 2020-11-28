from tkinter import *
import json

root = Tk()

#clicked button function
def myClick():
    myLabel = Label(root, text="Look! I clicked the button!")
    myLabel.grid(row=3, column=0)

#creating lable widget
myLabel1 = Label(root, text="Welcome to trivia!")
myLabel2 = Label(root, text="My name is Diana.")
#question = Label(root, text=)
submitButton = Button(root, text="submit your answer", command=myClick, bg="blue")

#placing elements into the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

submitButton.grid(row=2, column=0)

root.mainloop()