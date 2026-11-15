##de un numero ingresado por el usuario muesttras los numeros pares del 1 hasta el n
n = int(input('Digite un numero entero: '))

for elem in range(1,n + 1):
    if elem % 2 == 0:
        print(elem)



## contador inteligente, de un numero ingresado por el usuario digitar cuantos numeros 
## son pares he inpares

n2 = int(input('ingrese un numero: '))

contPares = 0;
contImpares = 0;

for elem in range(1, n2 + 1):
    if elem % 2 == 0:
        contPares += 1;
    else:
        contImpares += 1

print(f'total de numeros pares: {contPares}')
print(f'total numeros impares: {contImpares}')

##filtrar listas: dada una lista, crea una nueva lista con solo numeros positivos

numeros = [10, -5, 0, 20, -3, 7]

listaPares= []

for elem in numeros:
    if elem >= 0:
        listaPares.append(elem)

print(f'lista solo pares: {listaPares}')

##sacar el numero mas grande de una lista

numeroMayor = -99999

for i in numeros:
    if i > numeroMayor:
        numeroMayor = i 

print(f'el numero mayor es: {numeroMayor} ')

## calculadora de propinas

cuenta = float(input('Ingrese el valor de la cuenta: '))

porcentaje = float(input('ingrese el porcentaje de propina ¿10...20..30...? : '))

propina = cuenta * (porcentaje / 100)
total = cuenta + porcentaje

print(f'------------resultado-----------------')

print(f'tu cuenta es de {cuenta}')
print(f'porcentaje propína {porcentaje}: ${propina}')
print(f'total a pagar {total}')


##suma
def suma(num1, num2):
    return num1 + num2

print(suma(10,3))





