"""##sets
# Los conjuntos se utilizan para almacenar varios elementos en una sola variable.

Un conjunto es uno de los cuatro tipos de datos integrados en Python que se 
utilizan para almacenar colecciones de datos, los otros 3 son Lista , Tupla y Diccionario 
todos con diferentes cualidades y usos.

Un conjunto es una colección desordenada , inmutable* y no indexada

* Nota: del conjunto Los elementos no se pueden cambiar, pero puedes eliminarlos.
artículos y agregar nuevos artículos.
##"""

miSets = {'hola','mundo', 1,1,2}
print(miSets)

print(miSets.add('suarez'))#agregamos un nueo alor al sets 
print(miSets)

print(miSets.pop())#eliminamos un elemento de la kolleksion 
print(miSets)

miSets.remove('hola')
print(miSets)

print(miSets.update())

print(len(miSets))

#recorre el set en busca del parameto pasado
print('mundo' in miSets)

print('############################## EJEMPLO #####################')

set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}
set3 = {11,12,13,14,15}

set4 = set1.union(set2,set3)
print(set4)
##otra forma de hacerlo
set5 = set1 | set2 | set3
print(set5)