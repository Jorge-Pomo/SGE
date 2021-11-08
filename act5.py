import random

# Recopilación de datos
num1 = int(input('Dime un número: '))
num2 = int(input('Dime un número mayor al anterior: '))

numRandom = random.randint(num1, num2)

numUsuario = int(input('Dime el numero que crees que es: '))

# Algoritmo
while(numUsuario != numRandom):
    if(numUsuario > numRandom):
        print('El numero random es menor que ', numUsuario)
    else:
        print('El numero random es mayor que ', numUsuario)
    
    numUsuario = int(input('Dime el numero que crees que es: '))

print('Acertaste!!! El numero random es: ', numRandom)