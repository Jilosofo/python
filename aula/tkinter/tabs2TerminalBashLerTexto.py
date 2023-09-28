import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox 


result = subprocess.run(["cat", "/home/rodrigo/Documentos/python/python/ansibleProj/sample.txt"], stderr=subprocess.PIPE, text=True)
print(result.stderr)

#Tela Principal
janela = Tk()
janela.geometry("500x400+700+200")

tab_control = ttk.Notebook(janela)

#Criar os tabs
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

#Tabs
tab_control.add(tab1, text='Server')
tab_control.add(tab2, text='Computer')


#Estrutura das tabs

def issue():
    subprocess.run("xterm -e ssh cosev@10.245.190.183", shell=True)
    messagebox.showinfo('SSH Paco', 'SSH Paco successfully!')
btn = Button(tab1, text="SSH Paco", command=issue, height=1, width=12)
btn.grid(column=2, row=8, sticky='news')

#Tab Computer
def issue():
    subprocess.run('sudo systemctl start pyload', shell=True)
    messagebox.showinfo('Start PyLoad', 'PyLoad Started successfully!')
btn = Button(tab2, text="Start PyLoad", command=issue, height=1, width=12)
btn.grid(column=1, row=1, sticky='news')
 
def issue():
    subprocess.run("sudo systemctl stop pyload", shell=True,)
    messagebox.showinfo('Stop PyLoad', 'Pyload Stopped successfully!')
btn = Button(tab2, text="Stop PyLoad", command=issue, height=1, width=12)
btn.grid(column=2, row=1, sticky='news')

def issue():
    subprocess.run("xterm -e /bin/bash -l -c htop", shell=True)
    messagebox.showinfo('Listar', 'Lista completa!')
btn = Button(tab2, text="Listar Pasta", command=issue, height=1, width=12)
btn.grid(column=1, row=2, sticky='news')

with open("/home/rodrigo/Documentos/python/python/ansibleProj/sample.txt", "r") as arquivo:
	arqTexto = arquivo.read()
print(arqTexto)

def issue():
    messagebox.showinfo('Texto', arqTexto)
btn = Button(tab2, text="Abrir Arquivo", command=issue, height=1, width=12)
btn.grid(column=1, row=3, sticky='news')


tab_control.pack(expand=1, fill='both') #Sem esse tab_control não exibe os tabs

janela.mainloop()