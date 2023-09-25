import tkinter as tk
import tkinter.simpledialog

root = tk.Tk() # create main window
#root.iconify() # minimize main window 
root.withdraw() # hide main window 

answer = tkinter.simpledialog.askstring("Question", 'Your name:')
print(answer)

#root.destroy()  # should work without it
#root.mainloop() # should work without it