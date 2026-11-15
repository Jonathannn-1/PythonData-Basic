"""Bucles while (mientras se cumpla la condición)
Repite mientras la condición sea True. Cuidado con bucles infinitos."""


"""contador = 0

while contador <= 3:
    print(f'copnatdor va por {contador}')
    contador += 1

print('saliste del bucle porque contador es mayor a 3')

##programa un controlador del bucle que el mismo usuario decida si quiere salirse del bucle

while True:

    respuesta = input('Quieres salirte del Bucle? (si/no): ').lower()

    if respuesta == 'si':
        print('saliste del bucle, chao')
        break 
    else:
        continue"""

## crear un programa que adivine el numero secreto en 3 intentos

"""numeroSecreto = 10
intentos = 0 + 1
intentosRestantes = 3

while intentos < 3 + 1 :
    numero = int(input('Adivina el numero secreto del 1 al 10, tienes 3 intentos :) ='))
    print(f'intento num: {intentos}')

    intentos += 1

    if numero == numeroSecreto:
        print(f'felicidades adivinaste el numero secreto {numeroSecreto} !!!!!')
        break
    else:
        if numero != numeroSecreto:
            intentosRestantes -= 1
            print(f'fallaste :( te quedan {intentosRestantes} intentos')
            continue"""



#####################-------------------- BUCLE FOR ----------------------------###########


for i in range(1, 11):      # 1 a 10
    print(i, end=" ")       # imprime en línea
    
for i in range(10, 0, -1):  # cuenta regresiva
    print(i, "...", sep="", end=" ")
print("¡Despegue! 🚀")


# Con enumerate → índice + valor

lenguajes = ["Python", "SQL", "Airflow", "DBT", "Spark"]
for idx, lenguaje in enumerate(lenguajes, start=1):
    print(f"{idx}. {lenguaje.upper()}")


##ejercicios:

"""Adivina el número (while + condicionales)
Genera un número secreto (usa import random; secreto = random.randint(1,100)).
Deja adivinar hasta acertar o 7 intentos."""

import random 


secreto = random.randint(1,1000)
intentos = 0 + 1

while intentos < 7 + 1:

    num = int(input('Adivine el numero secreto del (1-1000), tienes 7 intentos: '))
    print(f'Intento numero : {intentos}')
    intentos += 1

    if num == secreto:
        print('Adivinaste el numero secreto felicidades !!!!!')
        break
else:
    print('Lo siento se te acabaron los intentos :(')

print(f'el numero secreto era {secreto}')
    

"""Tabla de multiplicar (for + range)
Pide un número y muestra su tabla del 1 al 10 con formato bonito."""


tableNum = int(input('ingrese un numero para mostrarlo en tabla:'))

for elem in range(1,11):
    print(f'{tableNum} x {elem} = {tableNum * elem} ')

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


##mejorar el programa agregarloe funciones