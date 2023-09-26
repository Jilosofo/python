import tkinter as tk
import sys
from tkinter import ttk

def fechar(self, event=None):
    print('Fechando...')
    sys.exit()

root = tk.Tk()
#root.iconphoto(False, tk.PhotoImage(file=config.icone))
root.title('Ansible Painel')
root.geometry('900x550')  # se precisar

# TODO: passar aqui uma matriz para cada painel/matriz com as configs padrão
# para cada tela/TV
#root.painel.pack(fill="both", expand=True, side='left') # side="top", fill="both",
expand=True
#root.painel2.pack(fill="both", expand=True, side='right') # side="top", fill="both",
#expand=True
#root.botoes.pack(side='bottom')
root.barra_status.pack()
root.bind("q", fechar)


root.mainloop()
