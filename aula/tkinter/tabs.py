from tkinter import *
from tkinter import ttk
# Create an instance of Tk
window = Tk()
window.title("Delftstack")

# Create a tab control that manages multiple tabs
tabsystem = ttk.Notebook(window)

# Create new tabs using Frame widget
tab1 = Frame(tabsystem)
tab2 = Frame(tabsystem)

tabsystem.add(tab1, text='First Tab')
tabsystem.add(tab2, text='Second Tab')
tabsystem.pack(expand=1, fill="both")

label = Label(tab1,text="Welcome in Delftstack")

label.grid(column=1,
           row=1,
           padx=40,
           pady=40)
label2nd = Label(tab2, text="Now we are able to see another tab")
label2nd.grid(column=1,
            row=1,
            padx=40,
            pady=40)

window.mainloop()