# recopilación de datos
numeroBotes = int(input('Dime el numero de botes: '))
resu = numeroBotes

i = 0

# Algoritmo
while(i < numeroBotes):
    resu -= i
    i += 1
    if(resu == 0):
        break

if(resu != 0):
    print('Los ', numeroBotes, ' botes no se podran apilar')
else:
    print('Los ', numeroBotes, ' botes si que se podran apilar')