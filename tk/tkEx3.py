from tkinter import *
from tkinter import simpledialog
# Create an object of TK (tkinter window)
window = Tk()
window.geometry("200x200")
window.title("Deltstack")
def intdialogbox():
    # this method accepts integer and returns integer
    employee_age = simpledialog.askinteger("Input","Enter your age",parent=window)
    dialog_output = Label(window, text=f'Employee age is {employee_age}',font=('italic 12'))
    dialog_output.pack(pady=20)

dialog_btn=Button(window,text='dialog button',command=intdialogbox)
dialog_btn.pack()

window.mainloop()