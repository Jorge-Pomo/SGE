import random
import time

# recopilacion de datos
N = int(input('Dime el numero de preguntas que quieres '))
cont = 0

tiempo1 = time.time()

#algoritmo
for i in range(1, (N + 1)):
    x = int(random.random() * 10)
    y = int(random.random() * 10)

    print('¿Cuánto es ', x, ' por ', y, '? ')
    resu = input()

    calcul = x * y

    if(int(resu) == calcul):
        print('Has acertado')
        cont += 1
    else:
        print('Has fallado')

# tiempo inicial - tiempio final = tiempo de duración
tiempoFinal = time.time() - tiempo1
print('Has sacado un ', (cont*10)/N ,' sobre 10')
print('Has tardado ', tiempoFinal, 'en terminar')