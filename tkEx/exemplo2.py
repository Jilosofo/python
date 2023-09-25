from tkinter import *
import tkinter as tk
from tkinter import simpledialog

my_w = tk.Tk()
my_w.geometry("410x360")  
my_w.title("www.plus2net.com")  # Adding a title
#my_w.label(text="Hello World!").grid(column=0, row=0)
w = Label(my_w, text="Hello, Welcome to Studytonight!") # Create a label with words
w.pack() # Put the label into the window


my_i = simpledialog.askinteger("Input","Input an Integer",parent=my_w)
print(my_i)

my_w.mainloop()