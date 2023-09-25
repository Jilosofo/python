from tkinter import *
win = Tk() # Create the root (base) window 
win.geometry("400x400")
w = Label(win, text="Hello, Welcome to Studytonight!") # Create a label with words
w2 = Label(win, text="Parte 2 hello, Welcome to Studytonight!") # Create a label with words
w.pack() # Put the label into the window
w2.pack() # Put the label2 into the window

win.mainloop()# Start the event loop