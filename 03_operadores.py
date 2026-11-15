##operadores aritmeticos##

print(2-9);
print(2+2);
print(34/23);
print(9%4);
print(4*5);
print(2//45)
print(2**3)

##concatenar informacion conek sigbo de mas (+) no siempre se puede realizar esa concatenacion
##solo se puede concatenar cuando son el mismo tipo de datos.

print('hola ' + '5' )
print('hola ' * 5)
print('hola ' * (2**3))

##operadores relacional
print(5 == 5); ##igual
print(5 < 5); ## menor que
print(4 > 6) ##mayor que
print(10 >= 7) ## mayor igual que
print(3 <= 5) ## menor igual que
print(30 != 30) # diferente de

##operadores logicos
print(2==2 and 2>1);
print(10 <= 20 or 1 != 1)
print(not(2>1))

var = 0  # Asignando 0 a var
print(var != 0)

var = 1  # Asignando 1 a var
print(var != 0)

##--------------------------operadores IN y NOT IN

"""
Python ofrece dos operadores muy poderosos, capaces de revisar la lista para verificar 
si un valor específico está almacenado dentro de la lista o no.

IN:
El primero de ellos (in) verifica si un elemento dado (el argumento izquierdo)
está actualmente almacenado en algún lugar dentro de la lista (el argumento derecho) 
- el operador devuelve True en este caso.

NOT IN:
El segundo (not in) comprueba si un elemento dado (el argumento izquierdo) está ausente
en una lista - el operador devuelve True en este caso.
"""

##REALIZAR UN PROGRAMA QUE ELIMINE LOS NUMEROS DUPLICADOS DE UNA LISTA

miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]


for i in miLista:
    copia = miLista
    if i in copia:
        del miLista[i]


print("La lista con elementos únicos:")
print(miLista)

##listas
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)

print('----------------------------------examen------------------------------')
my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])





















