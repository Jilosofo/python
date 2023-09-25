from aula.oo_pessoa2 import Pessoa2
##Ex2 from aula.init_python import Pessoa
## from aula pasta(package) e o init_python o arquivo py para leitura import classe dentro desse arquivo py
from aula.oo_pessoa import Pessoa1
## from o arquivo py e a classe desse arquivo py

pessoa1 = Pessoa1("Maria", 25)

print(pessoa1.nome) # "Maria"
print(pessoa1.idade) # 25


# Instancia um objeto da Classe "Pessoa"
pessoa2 = Pessoa2(nome='João', idade=25, altura=1.88)

# Chama os métodos de "Pessoa"
pessoa2.dizer_ola()
pessoa2.cozinhar('Spaghetti')
pessoa2.andar(750.5)