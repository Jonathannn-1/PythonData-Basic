## juego de adivinanzas 

import random

def juego_adivinanzas():

    print('......Bienvenido a juego de las adivinanzas......')
    numero_secreto = random.randint(1,1000)
    intentos = 0
    max_intentos = 7
    gano = False

    while intentos < max_intentos:
        try:
            numero = int(input('Ingrese un numero, tienes 7 oportunidades para adivinar el numero secreto (1-1000): '))
        except ValueError:
            print('ingrese un numero valido')
            continue
            
        intentos += 1
        print(f'intento {intentos}')

        if numero == numero_secreto:
            print(f'Felicidades, has adivinado el numero secreto {numero} !! ')
            gano = True
            break
        elif numero < numero_secreto:
            print('ush, mas arriba')
        elif numero > numero_secreto:
            print('ush, mas abajo')
    
    if not gano:
        print(f'Lo siento se te acabaron los intentos, el num secrero era {numero_secreto}')

def menu1():
    print('----Bienvenido al menu de juego----')
    
    while True:
        print('1. juego de adivinanzas')
        print('2. juego tablas de multipicar')
        print('3. salir de los juegos')
        opcion = input('Elija una opcion (1-3): ')

        if opcion == '1':
            juego_adivinanzas()
        elif opcion == '2':
            try:
                num_tabla = int(input('Ingrese el numero de la tabla que quiere mostrar:'))
                for i in range(1,11):
                    print(f'{num_tabla} x {i} = {num_tabla*i}')
            except ValueError:
                print('Ingrese un numero valido')
        elif opcion == '3':
            print('Adios, nos vemos pronto !!!')
            break
        else: 
            print('Opcion invalida',' xxxxx')

menu1()


"""FizzBuzz clásico (for + condicionales)
Imprime del 1 al 100:
Múltiplo de 3 → "Fizz"
Múltiplo de 5 → "Buzz"
Ambos → "FizzBuzz"

Sino → el número
Versión moderna (concatenación, más eficiente):"""

for i in range(1, 100):

    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')

    if (i % 3 == 0 and i % 5 == 0):
        print('FizzBuzz')
    else:
        print(f'{i}')
