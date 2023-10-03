import tkinter as tk
from tkinter import simpledialog
my_w = tk.Tk()
my_w.geometry("410x360")  
my_w.title("www.plus2net.com")  # Adding a title

my_i = simpledialog.askinteger("Input","Input an Integer",parent=my_w)
print(my_i)

my_w.mainloop()