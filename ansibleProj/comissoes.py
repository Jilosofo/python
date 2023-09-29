from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
#from plenario_comissoes import *
#from plenario_comissoes 

#janela = Tk()
janela = tb.Window(themename="superhero")

janela.title("Ansible!")
#janela.iconbitmap('images/codemy.ico')
janela.geometry('750x750')

label1 = tb.Label(janela, text="Gerenciador Ansible", font=("Helvetica", 28), bootstyle="light")
label1.pack(pady=10)

#Separador
my_sep = tb.Separator(janela, bootstyle="warning", orient="horizontal")
my_sep.pack(fill="x", padx="1") # fill x  dividi toda a janela


#teste

##10.245.128.90
janela.mainloop()