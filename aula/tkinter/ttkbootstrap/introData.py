from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

#janela = Tk()
janela = tb.Window(themename="superhero")

janela.title("TTK Bootstrap!")
#janela.iconbitmap('images/codemy.ico')
janela.geometry('500x350')

minha_data = tb.DateEntry(janela, bootstyle="default")
minha_data.pack(pady=10)




janela.mainloop()