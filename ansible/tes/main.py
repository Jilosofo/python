from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from tkinter import messagebox
import sys
import subprocess

janela = tb.Window(themename="superhero")
janela.title("Ansible!")
#janela.iconbitmap('images/codemy.ico')
#janela.geometry('750x650')
window_height = 700
window_width = 900

screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
#janela.iconbitmap('images/codemy.ico')
janela.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
#janela.geometry('750x750')
#from comissoes import *
#from plenario_comissoes 

###Criar Janela
#janela = Tk()

def plenario1():
    plenario1 = plenario(plen=1) #
    plenario1.janela_comissoes() #

def plenario2():
    plenario2 = plenario(plen=2) #
    plenario2.janela_comissoes() #


def janela_principal():
    label1 = tb.Label(janela, text="Gerenciador Ansible Comissões", font=("Helvetica", 28), bootstyle="light")
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

    #button1 = tb.Button(frame1,text="Plenário 1", bootstyle="sucess, outline", command=plenario(plen=1), plenario.janela_comissoes)
    # def plenario1():
    #     #subprocess.run("ssh sweetth@192.168.1.99 sudo systemctl reboot", shell=True)
    #     plenario1 = plenario(plen=1) #
    #     #print(plenario1)
    #     plenario1.janela_comissoes() #
    #     #messagebox.showinfo('Plenário')
    button1 = tb.Button(frame1,text="Plenário 1", bootstyle="sucess, outline", command=plenario1)
    button1.pack(pady=2, fill="x")
    button2 = tb.Button(frame1,text="Plenário 2", bootstyle="sucess, outline", command=plenario2)
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

    frame2 = tb.Labelframe(janela, bootstyle="light")
    #frame1.pack(side=LEFT, fill=BOTH, expand=True)
    frame2.pack(pady=1, padx=1)
    frame2.place(x=210,y=73, width=800, height=600)

    frame3 = tb.Labelframe(janela, bootstyle="light" , text="Comissões")
    frame3.pack(side=LEFT, fill=BOTH, expand=True)
    frame3.place(x=320,y=303, width=230, height=100)

    texto_orietacao = Label(frame3, text="==================")
    texto_orietacao.pack(pady=2)
    button2 = tb.Button(frame3,text="Todas Comissões", bootstyle="sucess, outline")
    button2.pack(pady=2, fill="x")


    ##10.245.128.90

    janela.mainloop()


def btn_browser():
    subprocess.run("xterm -e ansible-playbook -i /home/rodrigo/Documentos/ansible/ansible-pautaeletronica-des/hosts-tes /home/rodrigo/Documentos/ansible/ansible-pautaeletronica-des/pauta-playbook.yml", shell=True)
    messagebox.showinfo('ansible', 'ansible successfully!')
    print('Fechando...')
    sys.exit()

def btn_browser_pres():
    subprocess.run("xterm -e ansible-playbook -i /home/rodrigo/Documentos/ansible/ansible-pautaeletronica-des/hosts-tes /home/rodrigo/Documentos/ansible/ansible-pautaeletronica-des/pauta-playbook.yml", shell=True)
    messagebox.showinfo('ansible', 'ansible successfully!')
    print('Fechando...')
    sys.exit()

class plenario():

    def __init__(self, plen):
        self.plen = plen

    def janela_comissoes(self):

       
        label1 = tb.Label(janela, text="Gerenciador Ansible Comissões", font=("Helvetica", 28), bootstyle="light")
        label1.pack(pady=10)

        # default labelframe style Comissões
        frame1 = tb.Labelframe(janela, bootstyle="light" , text=f"Plenário {self.plen}")
        #frame1.pack(side=LEFT, fill=BOTH, expand=True)
        frame1.pack(pady=1, padx=1)
        frame1.place(x=9,y=73, width=200, height=600)
        
        frame2 = tb.Labelframe(janela, bootstyle="light")
        #frame1.pack(side=LEFT, fill=BOTH, expand=True)
        frame2.pack(pady=1, padx=1)
        frame2.place(x=210,y=73, width=800, height=600)

        texto_orietacao = Label(frame1, text="=======================")
        texto_orietacao.pack(pady=2)
        ## Button
        btn = Button(frame1, text="Comuns", command=btn_browser, height=1, width=12)
        btn.pack(pady=2, fill="x")  
        
        btn = Button(frame1, text="RDP", command=btn_browser, height=1, width=12)
        btn.pack(pady=2, fill="x") 

        btn = Button(frame1, text="ZOOM", command=btn_browser, height=1, width=12)
        btn.pack(pady=2, fill="x") 

        btn = Button(frame1, text="IP Servidor", command=btn_browser, height=1, width=12)
        btn.pack(pady=2, fill="x") 

        btn = Button(frame1, text="Atualizar Browser", command=btn_browser, height=1, width=12)
        btn.pack(pady=2, fill="x")
    
        btn = Button(frame1, text="Atualizar Browser Presidente", command=btn_browser_pres, height=1, width=12)
        btn.pack(pady=2, fill="x")   

        btn = Button(frame1, text="Voltar", command=janela_principal, height=1, width=12)
        btn.pack(pady=2, fill="x")   
        
        janela.mainloop() ## Fim


teste1 = plenario(plen="1")
print("Teste")
print(teste1.plen)
print("=====")


# def plenario1():
#     #janela_principal()
#     plenario1 = plenario(plen=1) #
#             #print(plenario1)
#     plenario1.janela_comissoes() 
janela_principal()
#plenario1()