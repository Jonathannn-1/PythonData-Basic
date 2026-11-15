##escribe un programa que indique el hola mundo en python

print('Hola Mundo')

saludo = 'Hola Mundo'
print(saludo)

##nomnbre usuario solicitado al usuario 

nombre = input(str('Escriba su nombre: '))

print('Hola', nombre)
##operacion aritmetica
print(((2+3)/(2*5))**2)

##programa que calcule horas trabajas y el pago que recibe por cada hora

horas = int(input('Digite las horas trabajadas: '))
valor = int(input('¿Cuanto te pagan por horas?: '))
print(horas * valor)

##ESCRIBIR UN PROGRAMA QUE LEA UN NUMERO ENTERO POSITIVO (n) Y DESPUES 
## muesre en pantalla la sujma de todos los enteros desde el 1 hasta el (n)

numero = int(input('Digite un numero entero positivo: '))
suma = numero * (numero + 1)/2

print('La suma del numero entero positivo', numero, 'mas', suma)

##calcular el IMC

peso = float(input('ingresa tu peso: '))
altura = float(input('ingrese tu altura: '))
elevar = altura **2
imc = peso / altura

print(f'tu indice se masa corporal es {round(imc,2)}')

##crear un programa que reciba dos numeros enteros un dividendo y un divisor 
## y tiene que devolver el cociente y resto de su misma division

n = int(input('ingrese el dividendo (n): '))
m = int(input('ingrese el divisor (m): '))

c = n // m
r = n % m

print(f'la division entre {n} y {m} da como cociente {c} y resto {r}')

##Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el 
# número de años, y muestre por pantalla el capital obtenido en la inversión.


invertir = int(input('Ingrese la cantidad a invertir:'))
interes_anual = float(input('ingrese el interes anual: '))
anios = int(input('años que dejara el dinero invertido: '))

a = invertir * (1 + (interes_anual / 100))**anios
 
print(f'tu capitar a adquirir en una inversion de {invertir} con un interes anual de {interes_anual} a {anios} años es de {round(a,2)}')



##jugueteria

peso_payaso = 112;
peso_muneca = 75;

cantidad_payasos = int(input('introduzca la cantidad de payasos vendidos: '))
cantidad_munecas = int(input('cantidad de muñecas vendidas'))

peso_total = (peso_payaso * cantidad_payasos) + (peso_payaso + cantidad_munecas)

print(f'cantidad de gramas venidos es de {peso_total}')

#conversiona kilos

print(f'kilos venidos {peso_total / 1000}')


#programa que calcule el interes anual 

deposita = int(input('ingrese la cantidad de dinero a depositar:'))

interes = 0.04

balance = deposita * (1 + interes)

print(f'balance del primer año {round(balance,2)}')

balance = balance * (1+interes)
print(f'balance del segundo año {round(balance,2)}')

balance = balance * (1 + interes)
print(f'balance del tercer año')

##Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el 
# programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca
#  y el coste final total.


barras_vendidas = int(input('ingrese el numero de barras vendidas: '))

##control basico de




