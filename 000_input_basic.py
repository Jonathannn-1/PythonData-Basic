nombre = str(input('Ingrese su nombre: ')).strip()
edad = int(input('Ingrese su edad: '))
print(f'Mi nombre es {nombre} y tengo {edad} años.')


##while loops

contador = 0;

while contador < 5:
    print('Contador:', contador)
    contador += 1
print('salimos del bucle')

#ciclo for 

frutas = ['Manzana', 'pera', 'Banana', 'Naranja']

for i in frutas:
    print(i,end=',')

#otras formas

respuesta = ''

while respuesta != 'salir':
    respuesta = input('Ingrese un comando para salir: ')
print('saliste el bucle')

#while con bandera con Break

bandera = True

while bandera:
    numero = int(input('Numero(0==salir): '))
    if numero == 0:
        break
    print('ingresaste', numero)
print('saliste!! hasta luego')


# palabra reservada continue: la palabra reservada salta iteraciones e inicia una nueva

lista_nueva = []
for j in range(5):
    if j == 2:
        continue
    lista_nueva.append(j)
print(lista_nueva)
#salisa= [0,1,3,4]

#eliminando lista

lista = ['x','x','x','x']

while 'x' in lista:
    lista.remove('x')
print(lista)