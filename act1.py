# recopilación de datos
num1 = int(input('Dime el primer número '))
num2 = int(input('Dime el segundo número '))

num2 += 1

# Algoritmo
for i in range (num1, num2) :
    if(i % 2 == 0):
        print(i)