#
# funciones: se usan para encapsular una logica en concreto para reslver un problema
# y asi evitar volver a repetir una logica#

##funcion que recibe un parametro
def miFundcion(name):
    print(name)

miFundcion('jonathan')##llamada de la funcion

#funcion
def miFuncion2 ():
    print('hola, mi funcion en python')

miFuncion2()##llamada de la funcion

##suma dos valores
def suma(num1,num2):
    return num1 + num2

print(suma(4,5))

#parseando los datos y pasandole datos por defecto
def datos(nombre, apellido, novia = 'dayana'):
    return(f'mi nombre es {nombre} y mi apellido es {apellido} y mi nvoia es {novia}')

print(datos('jona','mon'))

#imprime multiples parametros del mismo tipo de datos
def multiples(*nombres):
    print(type(nombres))
    for elemnt in nombres:
        print(elemnt.upper())

multiples('jonathan','dayana','jessica')


################ FUNCIONES PARAMETRIZADAS #############################


""""
El potencial completo de una función se revela cuando puede ser equipada con una interface que es capaz de aceptar
datos provenientes de la invocación. Dichos datos pueden modificar el comportamiento de la función, haciéndola más
flexible y adaptable a condiciones cambiantes.

Un parámetro es una variable, pero existen dos factores que hacen a un parámetro diferente:

* los parámetros solo existen dentro de las funciones en donde han sido definidos, y el único lugar donde un
     parámetro puede ser definido es entre los paréntesis después del nombre de la función, donde se encuentra 
     la palabra clave reservada def;
* la asignación de un valor a un parámetro de una función se hace en el momento en que la función se manda llamar
     o se invoca, especificando el argumento correspondiente.
"""

##parametros posicionales: imrpimer el orden que le pasen en el print sin importar el orden de parame5ros en la llamada
def induccion(primer_nombre, primer_apellido):
    print("Hola, mi nombre es", primer_nombre, primer_apellido)

induccion(primer_nombre = "James", primer_apellido = "Bond")
induccion(primer_apellido=  "Skywalker", primer_nombre = "Luke")

#####################################   ejercicios    ##########################################

## año bisiesto

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f'{year} es año bisiesto')
    else:
        print(f'{year} no es año bisiesto')

is_year_leap(2000)

##calular IMC
def calcularIMC(peso,altura):
    imc = peso / altura **2
    print(imc)

calcularIMC(73,186)