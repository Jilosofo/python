#from pessoas import Pessoa
from pessoas import *

# Instancia um objeto da Classe "Pessoa"
pessoa = Pessoa(nome='João', idade=25, altura=1.88)

# Chama os métodos de "Pessoa"
pessoa.dizer_ola()
pessoa.cozinhar('Spaghetti')
pessoa.andar(750.5)

def testando():
    teste1 = teste(plen=21)
    teste1.teste1()

testando()
#print("Teste")
#print(teste1.plen)
#print("=====")