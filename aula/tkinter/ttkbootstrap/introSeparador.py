from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

#janela = Tk()
janela = tb.Window(themename="superhero")

janela.title("TTK Bootstrap!")
#janela.iconbitmap('images/codemy.ico')
janela.geometry('950x750')

label1 = tb.Label(janela, text="Label 1", bootstyle="light")
label1.pack(pady=40)

#Separador
my_sep = tb.Separator(janela, bootstyle="danger", orient="horizontal")
my_sep.pack(fill="x", padx="10") # fill x  dividi toda a janela

label2 = tb.Label(janela, text="Label 2", bootstyle="light")
label2.pack(pady=40)

# default labelframe style
frame1 = tb.Labelframe(janela, bootstyle="light" , text="Label 1 Frame")
frame1.pack(pady=40)

texto_orietacao = Label(frame1, text="===== Label comum!!! =====")
texto_orietacao.pack()


# info colored labelframe style
#Labelframe(bootstyle="info")


janela.mainloop()
