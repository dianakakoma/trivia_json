from tkinter import *

root = Tk()

#creating lable widget
myLabel1 = Label(root, text="Welcome to trivia!")
myLabel2 = Label(root, text="My Name is Diana.")

#shoving it into the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()