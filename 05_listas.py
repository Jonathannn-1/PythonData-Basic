#las listas son una estructura para guardar un conjunto de datos

mi_lista =  [
    'jonathan',
    23,
    1.87,
    1007117760
]

#llamado de las listas
print(len(mi_lista))#muestra la longitud de la lista
print(type(mi_lista))
print(mi_lista)
print(mi_lista[3])#busco la posicion de la lista

print(mi_lista.count('jonathan'))
#suma por elementos de una lista
print(mi_lista[1] + mi_lista[1])

#agrega un nuevo valor a la lista.
mi_lista.append('Montes');
print(mi_lista)

#inserto un nuevo valor en la posicion que deseo.
mi_lista.insert(0, 'negro')
print(mi_lista)

#elimina el valor en la posicion pasada.
print(mi_lista.remove('Montes'))
print(mi_lista)
mi_lista.append('Montes');

#elimina un elemento en concreto si no se le pasa el elemento elimina el ultimo
#como por defecto
print(mi_lista.pop(0))
print(mi_lista)
var = 'ban'
print(mi_lista.append(var))
print(mi_lista)

#copiando la lista existente
mi_lista_copiada = mi_lista.copy()
print(mi_lista_copiada)

#lista inversa
mi_lista_copiada.reverse()
print(mi_lista_copiada)

#reordena
"""
mi_lista_copiada.sort()
print(mi_lista_copiada)
"""

print('################################## USANDO LISTAS vacias ###################')

lista_vacia = []

for i in range(0,5):
    lista_vacia.append(i + 1)
print(lista_vacia)

lista_vacia2 = []

for j in range(0, 10):
    lista_vacia2.insert(0, j + 1)

print(f'imprimimos lista = {lista_vacia2}')

## indexado sin len
miLista = [10,8,7,70,2,4]
suma = 0

for d in miLista:
    suma += d

print(suma)


print('""""""""""""""""""""""""ORDENAMIENTO BURBUJA""""""""""""""""""""""""""""""""')

"""el ordenamiento burbuja consiste en rodenar de menor a mayor una lista de numeros
"""

my_list = [8, 10, 6, 2, 4]  # lista a ordenar

for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
    if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.
print(my_list) 

##forma con metodos
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list) 

## si quieres sacarlos en reversa es con el metodo reverse

my_list.reverse()
print(my_list)