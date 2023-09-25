# Importing Tkinter
from tkinter import *
from tkinter import ttk
# Importing ThemedTK library
from ttkthemes import ThemedTk

# Creating root window
# root = Tk()
root = ThemedTk(theme="arc")

# Setting Window width and height
root.geometry('400x600')
# Creating a button widget
mybutton = ttk.Button(root, text='Hello world!!!')
# showing at the center of the screen
mybutton.place(relx=0.5, rely=0.5, anchor=CENTER)

# runnning the app
root.mainloop()