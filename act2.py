# recopilación de datos
contraseña = str(input('Dime la contraseña '))
contraseñaRepetida = str(input('Repite la contraseña '))

cont = 0

# Algroitmo
while contraseña != contraseñaRepetida :
    print('¡ERROR! las contraseñas no  coinciden ')
    contraseñaRepetida = str(input('Repite la contraseña '))
    cont += 1

    if cont == 5:
        print('Las contraseñas no coinciden. Vuelve a intentarlo')
        break

print('Las contraseñas coinciden')
