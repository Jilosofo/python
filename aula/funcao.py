# Criando a função:
def funcao():
    print("Funções em Python")
# Chamando a função criada:
funcao()

# Criando a função:
def dobrar(x):
    print(x * 2)
# Chamando a função criada:
dobrar(15)

 # Criando a função:
def dobrar(x):
     x *= 2
     return x
 # Chamando a função criada:
a = dobrar(15)
print(a)
print(dobrar(30))