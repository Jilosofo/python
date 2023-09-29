from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import subprocess
from tkinter import messagebox 

def btn_browser():
    subprocess.run("xterm -e ansible-playbook -i /home/rodrigo/Documentos/ansible/ansible-pautaeletronica-des/hosts-tes /home/rodrigo/Documentos/ansible/ansible-pautaeletronica-des/pauta-playbook.yml", shell=True)
    messagebox.showinfo('SSH Paco', 'SSH Paco successfully!')

class plenario:
    def __init__(self, plen):
      self.plen = plen

    def janela_comissoes(self):
        janela = tb.Window(themename="superhero")
        janela.title("Ansible!")
        #janela.iconbitmap('images/codemy.ico')
        janela.geometry('750x750')

        label1 = tb.Label(janela, text="Gerenciador Ansible Comissões", font=("Helvetica", 28), bootstyle="light")
        label1.pack(pady=10)

        #Separador
        my_sep = tb.Separator(janela, bootstyle="warning", orient="horizontal")
        my_sep.pack(fill="x", padx="1") # fill x  dividi toda a janela

        label2 = tb.Label(janela, text=f"---{self.plen}--", bootstyle="light") 
        label2.pack(pady=1)

        # default labelframe style Comissões
        frame1 = tb.Labelframe(janela, bootstyle="light" , text=f"Plenário {self.plen}")
        #frame1.pack(side=LEFT, fill=BOTH, expand=True)
        frame1.pack(pady=1, padx=1)
        frame1.place(x=9,y=73, width=200, height=600)

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
    
        btn = Button(frame1, text="Atualizar Browser Presidente", command=btn_browser, height=1, width=12)
        btn.pack(pady=2, fill="x")   

        
        janela.mainloop() ## Fim
    

   
    
#btn2 = Button(text="Plenário 1", command=plenario1, height=1, width=12)
#btn2.pack(pady=2, fill="x")
#btn2.grid(frame1,column=1, row=2, sticky='news')
#plenario1 = plenario(plen=1)
#plenario1.janela_comissoes()
    ##10.245.128.90

    