from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class principal:
    def janela_principal():
        janela = tb.Window(themename="superhero")
        janela.title("Ansible!")
        #janela.iconbitmap('images/codemy.ico')
        janela.geometry('750x750')

        label1 = tb.Label(janela, text="Gerenciador Ansible", font=("Helvetica", 28), bootstyle="light")
        label1.pack(pady=10)

        #Separador
        my_sep = tb.Separator(janela, bootstyle="warning", orient="horizontal")
        my_sep.pack(fill="x", padx="1") # fill x  dividi toda a janela

        label2 = tb.Label(janela, text="-----", bootstyle="light") 
        label2.pack(pady=1)

        # default labelframe style Comissões
        frame1 = tb.Labelframe(janela, bootstyle="light" , text="Comissões")
        #frame1.pack(side=LEFT, fill=BOTH, expand=True)
        frame1.pack(pady=1, padx=1)
        frame1.place(x=9,y=73, width=200, height=600)

        texto_orietacao = Label(frame1, text="=======================")
        texto_orietacao.pack(pady=2)
        
        janela.mainloop()
        
