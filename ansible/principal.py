from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from comissoes import *

#from comissoes import *
#from plenario_comissoes 

###Criar Janela
#janela = Tk()
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
    ## Button
#def plenario1:

    button1 = tb.Button(frame1,text="Plenário 1", bootstyle="sucess, outline", command=teste(plen=1))
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 2", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")
    button1 = tb.Button(frame1,text="Plenário 3", bootstyle="sucess, outline")
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 4", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")
    button1 = tb.Button(frame1,text="Plenário 5", bootstyle="sucess, outline")
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 6", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")
    button1 = tb.Button(frame1,text="Plenário 7", bootstyle="sucess, outline")
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 8", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")
    button1 = tb.Button(frame1,text="Plenário 9", bootstyle="sucess, outline")
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 10", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")
    button1 = tb.Button(frame1,text="Plenário 11", bootstyle="sucess, outline")
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 12", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")
    button1 = tb.Button(frame1,text="Plenário 13", bootstyle="sucess, outline")
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 14", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")
    button1 = tb.Button(frame1,text="Plenário 15", bootstyle="sucess, outline")
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 16", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")

    # info colored labelframe style
    #Labelframe(bootstyle="info")

    # default labelframe style
    frame2 = tb.Labelframe(janela, bootstyle="light" , text="Comissões")
    frame2.pack(side=LEFT, fill=BOTH, expand=True)
    frame2.place(x=320,y=303, width=230, height=100)

    texto_orietacao = Label(frame2, text="==================")
    texto_orietacao.pack(pady=2)
    button2 = tb.Button(frame2,text="Todas Comissões", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")


    ##10.245.128.90

    janela.mainloop()

teste1 = teste(plen="1")
print("Teste")
print(teste1.plen)
print("=====")

janela_principal()