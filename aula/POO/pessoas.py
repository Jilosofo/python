from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import subprocess
from tkinter import messagebox 


class Pessoa:
  def __init__(self, nome: str, idade: int, altura: float):
    self.nome = nome
    self.idade = idade
    self.altura = altura

  def dizer_ola(self):
    print(f'Olá, meu nome é {self.nome}. Tenho {self.idade} '
          f'anos e minha altura é {self.altura}m.')

  def cozinhar(self, receita: str):
    print(f'Estou cozinhando um(a): {receita}')

  def andar(self, distancia: float):
    print(f'Saí para andar. Volto quando completar {distancia} metros')

class teste:
    def __init__(self, plen):
      self.plen = plen 

    def teste1(self): # Lembrando que o def tem que está alinhado com def de cima
        print(f"Teste qual plenário: {self.plen}")
        janela = tb.Window(themename="superhero")
        janela.title("Ansible!")
        #janela.iconbitmap('images/codemy.ico')
        janela.geometry('750x750')

        label1 = tb.Label(janela, text="Gerenciador Ansible Comissões", font=("Helvetica", 28), bootstyle="light")
        label1.pack(pady=10)

        #Separador
        my_sep = tb.Separator(janela, bootstyle="warning", orient="horizontal")
        my_sep.pack(fill="x", padx="1") # fill x  dividi toda a janela

        label2 = tb.Label(janela, text=f'--{self.plen}---', bootstyle="light") # Lembrete colocar o (f) na frente para poder ler
        label2.pack(pady=1)
        
        janela.mainloop()

# Agora vamos explicar “tintim por tintim”:

# Temos a definição da Classe na primeira linha com class Pessoa. Isso diz ao Python que vamos criar a definição de uma nova classe.
# Em seguida, temos o método __init__. Ele é muito importante e é chamado de Construtor. Ele é chamado ao se instanciar objetos e é nele que geralmente setamos os atributos do objeto.
# Em seguida temos a definição dos métodos dizer_ola(), cozinhar() e andar().
# Perceba que no método dizer_ola() referenciamos os atributos do próprio objeto com o argumento self: self.nome, self.idade e self.altura.