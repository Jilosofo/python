from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

#janela = Tk()
janela = tb.Window(themename="superhero")

janela.title("Ansible!")
#janela.iconbitmap('images/codemy.ico')
janela.geometry('950x750')

label1 = tb.Label(janela, text="Gerenciador Ansible", font=("Helvetica", 28), bootstyle="light")
label1.pack(pady=10)

#Separador
my_sep = tb.Separator(janela, bootstyle="warning", orient="horizontal")
my_sep.pack(fill="x", padx="1") # fill x  dividi toda a janela

label2 = tb.Label(janela, text="Label 2", bootstyle="light")
label2.pack(pady=1)

# default labelframe style
frame1 = tb.Labelframe(janela, bootstyle="light" , text="Plenário")
frame1.pack(side=LEFT, fill=BOTH, expand=True)
#frame1.place(x=30,y=53, width=120, height=350)
texto_orietacao = Label(frame1, text="===== Plenário!!! =====")
texto_orietacao.pack(pady=2)

texto_orietacao = Label(frame1, text="===== Comissõe!!! =====")
texto_orietacao.pack(pady=2)

# default labelframe2 style
frame2 = tb.Labelframe(janela, bootstyle="light" , text="Comissões")
frame2.pack(pady=1, padx=1, side="left", fill=BOTH, expand=True)

texto_orietacao = Label(frame2, text="===== Plenário!!! =====")
texto_orietacao.pack(pady=2)

texto_orietacao = Label(frame2, text="===== Comissõe!!! =====")
texto_orietacao.pack(pady=2)


# info colored labelframe style
#Labelframe(bootstyle="info")


janela.mainloop()