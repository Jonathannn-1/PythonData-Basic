"""
tuplas: la diferencia del  ls tuplas a las listas son los valores inmutables
no se pueden actualiza, ni eliminar ni insertar
"""

miTupla = (1,2,3,4,5,'hola')

print(miTupla)
print(type(miTupla))
print(miTupla.count(1))
print(miTupla.index(1))#busca el numero del indice del parametro pasado
print(miTupla[1:3])

##convertir una tupla a lista

tupla_a_lista = list(miTupla)

print(type(tupla_a_lista))
print(tupla_a_lista)
tupla_a_lista.insert(0,'h')
print(tupla_a_lista)
##ahora ya la tupla siendo una lista le podemos agregar cualquier metodo de las listas

del miTupla ##eliminando la varaible
##print(miTupla)

miTupla2 = (1,2,3,45,5,5,455)

print(miTupla2)
print(miTupla2.count(5))

#for con blucle 
for elem in miTupla2:
    print(elem)

print(miTupla2.index(5))



tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)# Escribe tu código aquí.
print('-----------------------------') 
print(duplicates) # salida: 4
  

print('---------convertir una lista a una tupla-------------')
my_list = ["car", "Ford", "flower", "Tulip"]

t =  tuple(my_list)
print(t)
print(type(t))
