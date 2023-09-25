st = 'Criar uma solução que essa frase só capture a letra s'

split_string = st.split()

for letra in split_string:
    if letra[0] == 's':
        print (letra)

print ("===== Próxima lista ====")

#Criar range que imprima so os numeros pares de 0 a 10

x = range(0,10)

for num in x:
    if num % 2 == 0:
        print (num)

print ("===== Próxima lista ====")

y = range(0,50)
for num in y:
    if num % 3 == 0:
        print (num)

print ("===== Próxima lista ====")

pt = [y for y in range(1,50) if y % 3==0]
print (pt)

print ("===== Próxima lista ====")

n = 0 # Declarar n aqui antes
st = 'Imprimir somente as palavra que tenha numeros par de caracteres'
split_string = st.split()
for i in split_string:
    n = n+1
    print (' ')
    print ('Numero:',n,')',' Palavra separada:',i)
    #print ('Texto completo:',split_string)
    size = len(i)
    print ('Tamanho de cada frase: ', size)
    print (" ")
    if size % 2 == 0:
        print (i, ':possui comprimento par!!!')
print ('')
print ("===== Próxima lista ====")
print ('Imprima as frases que for multiplo de 3 se for multiplo de 5 ou se ela for das duas')
for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        print('MultiDuas(3 e 5)')
    elif i % 3 == 0:
        print ('Multi3')
    elif i % 5 == 0:
        print ('Multi5')
    else:
        print (i)
print ('')
print ("===== Próxima lista ====")
print ('')
st = 'Criar uma lista das primeiras letras de cada palavra na string'
split_string = st.split()

list = [letter[0] for letter in split_string]
print (list)
