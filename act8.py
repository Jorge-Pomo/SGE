import random

# variables
contPC = 0
contUsu = 0

# algoritmo
while(contPC != 3 or contUsu != 3):
    print("Piedra Papel o Tijeras")
    resUsu = input()
    resUsu = resUsu.lower

    lista = ['piedra', 'papel', 'tijeras']
    resuPC = random.choice(lista)
    print(resuPC)

    if(resUsu == 'piedra'):
        if(resuPC == 'papel'):
            contPC += 1
        if(resuPC == 'tijeras'):
                contUsu += 1
    if(resUsu == 'tijeras'):
        if(resuPC == 'piedra'):
            contPC += 1
        if(resuPC == 'papel'):
            contUsu += 1
    if(resUsu == 'papel'):
        if(resuPC == 'tijeras'):
            contPC += 1
        if(resuPC == 'piedra'):
            contUsu += 1
    
    print("PC = ", contPC, " Uuario = ", contUsu)

    if(contPC == 3):
        break
    if(contUsu == 3):
        break
    

if(contPC == 3):
    print('Ha ganado el PC!!!!!')
else:
    print('Ha ganado el usuario!!!!')