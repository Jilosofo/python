#O método __init__ é um método especial em Python que é chamado automaticamente quando criamos um objeto.
#Dessa forma, o método pode está sendo utilizado para inicializar o objeto e atribuir valores aos seus atributos.
#Aqui estão alguns exemplos de como o método init pode está sendo utilizado em diferentes tipos de objetos em Python:
#
#
#class Pessoa:
#    def __init__(self, nome, idade):
#       self.nome = nome
#       self.idade = idade

#pessoa1 = Pessoa("Maria", 25)


#print(pessoa1.nome) # "Maria"
#print(pessoa1.idade) # 25
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

