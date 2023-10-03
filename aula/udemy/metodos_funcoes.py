
# Esqueva uma função que caucule o volume de uma esfera dado seu raio
def vol(rad):
    volume = (4/3) * 3.14 * (rad ** 3)
    return volume

# Escreva uma função que verifica se um numero está em um determinado intervalo(inclusive o maximo e minimo)
def ram_check(num, low, hight ):
    if num in range(low, hight):
        return True
    else:
        return False
# Se quando eu chamar a função ela for maio que 10 vai dá falso   
print (ram_check(10, 1, 10))
print("==================")
print("===== sensitive case =======")


s = "Olá sr Rorges, como vocês está bem, terça-feira?"

def up_low(a):
    up = 0
    low = 0
    
    for i in s:
        if  i.isupper():
            up += 1
            print("UP:",i)
        elif i.islower(): #elif aguarda instrução
            low += 1
            print("Low:",i)
        else:
            continue    
    print("Número de caracteres maiúsculos:",up)
    print("Número de caracteres minúsculos:",low)
up_low(s)
 
 
        

    


