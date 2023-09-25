from tkinter import *
from tkinter import simpledialog
# Create an object of TK (tkinter window)
window = Tk()
window.geometry("300x200")
window.title("Deltstack")
def floatdialogbox():
    # this method accepts float and returns float
    income_tax = simpledialog.askfloat("Input","Enter the tax",parent=window,minvalue=1.0,maxvalue=10.0)
    dialog_output = Label(window, text=f'Your tax is {income_tax} percent',font=('italic 12'))
    dialog_output.pack(pady=20)

dialog_btn=Button(window,text='dialog button',command=floatdialogbox)
dialog_btn.pack()

window.mainloop()