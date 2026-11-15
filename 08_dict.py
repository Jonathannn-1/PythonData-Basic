####
# los diccionarios son un conjunto de llave-valor#

dict = {
    'nombre': 'jonathan',
    'apellifo': 'montes',
    'edad': 23,
    'estatura': 187,
    'tupla': {'hola', 'mundo'},
    'lista': [1,2,3],
    'sets': {'pyhton','js', 'SQL'}
}

print(dict)

print(len(dict))
print(dict['lista'])

#agregamos un nueco valor
dict['numero'] = '3006503934'
print(dict)

##busca por llaves
print('numero' in dict)
##busca el elemento
print(dict['apellifo'])

print(dict.keys())
print(dict.items())
print(dict.values())


lenguajes = {'lenguaje1': 'js', 'lenguaje2': 'SQL', 'lenguaje3': 'python'}

for llave in lenguajes.keys():
    print('valor','->', lenguajes[llave])

for item in lenguajes.values():
    print(item)

##insertamos un nuevo lenguaje
lenguajes.update({'lenguaje4': 'java'})

print(lenguajes)

lenguajes.pop('lenguaje4')
print(lenguajes)

print('---------------------------------')
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    for clave, value in item.items():
        d3[clave]= value

print(d3)

print('------forma mas simple------')
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

print('-------------convertir tupla a un diccionario--------------------')
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = {}

for item,valor in colors:
    colors_dictionary[item]= valor

print('tu tupla a diccionario',colors_dictionary)

## declaramos un diccionario

Diccionario = {
    'nombre': 'Jonathan',
    'edad': 25,
    'sex': 'masuclino'
}

print(Diccionario['nombre'])
print(hash('nombre')%8)

print(Diccionario.get('edades','no encontrado'))

print('---------------------crear un bucle con num cuadrados----------------')
num_cuadrados= {}

for i in range(10):
    num_cuadrados[i]= i **2

print(num_cuadrados)

del Diccionario['edad']
print(Diccionario)

for clave,valor in num_cuadrados.items():
    print(clave,'->', valor)