from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

#janela = Tk()
janela = tb.Window(themename="superhero")

janela.title("TTK Bootstrap!")
#janela.iconbitmap('images/codemy.ico')
janela.geometry('500x350')

counter = 0
# Criar função para o button
def mudar():
    global counter
    counter += 1
    if counter % 2 == 0:
        texto1.config(text="Ola Mundo!!!")
    else:
        texto1.config(text="Ola mundo!!!!!")


## Colors:
## Defaultm primarym secondarym success, info, warning, danger,
## light, dark

###Criar label 
texto1 = tb.Label(janela,text="Olá Mundo",font=("Helvetica", 28), 
    bootstyle="light, inverse")
texto1.grid(column=0, row=0)
texto1.pack(pady=50)
button1 = tb.Button(janela,text="Click Aqui!!!", bootstyle="sucess, outline", command=mudar)
button1.pack(pady=20)
#texto_orietacao = Label(janela, text="===== Label comum!!! =====")
#texto_orietacao.grid(column=0, row=1, padx=200, pady=30) # padx largura pady altura
#Criar button


janela.mainloop() # Final da instrução