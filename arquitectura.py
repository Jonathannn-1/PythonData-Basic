# En este archivos vamos a ver la arquitectura de los objetos ne python


print('############## Arquitectura de listas ##############')

# las listas son mutables y se accese a su valor mediante indexacion

nombres = ['jona','dayana','annie']

#el metodo id devuelve el espacio en memoria es decir devuelve la referencia en memoria
print(id(nombres))

## aqui accederemos a un indice de la lista
print(nombres[0])
#accedemos a su referencia en memoria 
print(id(nombres[0]))

nombres[0] = 'antonio'
print(nombres)
print(id(nombres))
print(id(nombres[0]))

print('### Metodos de listas ###')

# metodo append inserta un valor a lo ultimo de la lista
nombres.append('Montes')
print(nombres)
#clear limpia la lista
#nombres.clear()
#print(nombres)
#metido copy crea una copia de la lista
nombres.copy()
print(nombres)


print(nombres.count('montes'))

##devuelve el numero de indice del objeto pasado
print(nombres.index('Montes'))

#inserta un nuevo objeto segun el indice pasado
nombres.insert(0,'python')
print(nombres)
#el pop elimina el ultimo indice de la lista
nombres.pop()
print(nombres)
#elimina el valor del indice pasado
nombres.remove('dayana')
print(nombres)
## devuelve la lista invertida
nombres.reverse()
print(nombres)

#ordena la lista, si esta en letras la ordena de forma alfabetica si esta en numero los ordena de forma ascendente
nombres.sort()
print(nombres)
numeros= [10,9,8,7,6,1,2,3,4,5]
numeros.sort()
print(numeros)


# si nos fijamosque la refencia del objeto lista no cambio su numero lo que cambio fue el valor de referencia de indexacion
#a esto nos referimos cuando se dice objeto mutable

#print('############# arquitectura tuplas ###############')

#las tublas son inmutables, es decir que cuando se asigna su valor no puede ser cambiado

miTupla = (1,2,3,4,5)
print(miTupla)

# para acceder a los valores de la tupla tambien es por indexacion
print(miTupla[0])

## este nos daria un error ya ue al decir que son inmutables sus valores no pueden ser cambiados
#miTupla[0] = 10

print(type(miTupla))


## arquiectura loops

lenguajes_programacion = ['Python','JavaScript','Java', 'Go']

for lenguaje in lenguajes_programacion:
    print(lenguaje)
    print('--------')

print('Salimos del bucle')