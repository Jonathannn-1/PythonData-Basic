#
# bien conocidos como controles de flujo para toma de decisiones#

##edad mayor a 18
edad = 18;

if edad >= 18:
    print('es mayor de edad')
else:
    print('es menor de edad')

#con operadores logcicos
num = 5*5

if edad > 10 and edad <= 25:
    print('el numero es mayor que y menor o igual a 25')
else: 
    print('es manyor que 25')

#elif

mi_lista = ['lunes','martes','miercoles', 'jueves','viernes']
diaSemana = mi_lista[4]

if mi_lista[0] == diaSemana:
    print('hoy es lunes')
elif mi_lista[1] == diaSemana:
    print('hoy es martes')
elif mi_lista[2] == diaSemana:
    print('hoy es miercoles')
elif mi_lista[3] == diaSemana:
    print('hoy es jueves')
elif mi_lista[4] == diaSemana:
    print('hoy es viernes')
else: 
    print('no es ningun dia de la semana')



number1 = int(input('digita un numero: '))
number2 = int(input('digita un numero: '))

##programa que busqie el numero mas grande.
 # Elige el número más grande
if number1 > number2: 
    larger_number = number1
else: 
    larger_number = number2
 
# Imprime el resultado
print("El número más grande es:", larger_number) 




######################### Se leen tres números buscamos el numero mas grande entre 3 numeros
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
largest_number = number1

# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > largest_number:
    largest_number = number2

# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number3 > largest_number:
    largest_number = number3

# Imprime el resultado.
print("El número más grande es:", largest_number)


year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
elif year % 4 != 0:
    print('año comun')
elif year % 100 != 0:
	print('año bisiesto')
elif year % 400 != 0:
	print('año comun')
else: 
	print('año bisiesto')