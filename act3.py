# recopilación de datos
anchoMaximo = int(input('Introduce N:'))

anchoMaximo += 1

# Algoritmo
for i in range(1, anchoMaximo):
    i += 1
    for j in range(1, i):
        print('*', end='')
    print()

anchoMaximo -= 1

for i in reversed(range(anchoMaximo)):
    for j in reversed(range(i)):
        print('*', end='')
    print()