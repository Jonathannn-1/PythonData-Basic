#
# loops: bien conocidos como bucles.: son usados cuando queremos repepetir un codigo
# cierta cantidad de veces#

# bucle while: mientras: mientras que se cumpla la condicion el bucle simepre va iterar
mi_varaible = 0;
while mi_varaible < 10:
    mi_varaible += 1; ##operador de incremento
    print(mi_varaible)
else:
    print('saliendo del while, variable es mayor a 10')

variable2 = 0

while variable2 < 10:
    variable2 += 2
    if variable2 == 8:
        print('stop')
        break;
print(variable2)

##FOR: SIRVE CUANDO QUEREMOS ITERAR UNA SECUENCIA DE ELEMENTOS
print('lista ##############################################################')

lista= [1,2,3,4,4,5]
for elementos in lista:
    print(elementos)

print('tuplas ##############################################################')

tupla = ('hola','mundo')
for elemento in tupla:
    print(elemento)

print('sets ##############################################################')

sets = {'jona','mont','sua'}
for elemento in sets:
    print(elemento)

print('DICCIONARIO ##############################################################')

dicc = {'nombre: jonathan', 'edad: 23', 'novia: dayana'}
for elemento in dicc:
    print(elemento)
    if elemento == 'novia':
        break;
    print(dicc)

diccionario = {1: 'python', 'edad': 23}

#continue
for elem in diccionario:
    print(diccionario)
    if elem == 'edad':
        continue;
else:
    print('stop')

print('#######################  NEW SECTION') 

# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", largest_number)

##contando
counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)


## bucle for
import time

for i in range(1,5):
    print(i, 'Mississippi')
    time.sleep(1)

print('Lista o no, aquí vengo!')


"""

break - sale del bucle inmediatamente, e incondicionalmente termina la operación del bucle; 
    el programa comienza a ejecutar la instrucción más cercana después del cuerpo del bucle.
continue - se comporta como si el programa hubiera llegado repentinamente al final del cuerpo;
    el siguiente turno se inicia y la expresión de condición se prueba de inmediato.

"""