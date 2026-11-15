lista_email = ['jona@gmail.com','',None,'person@gmail.com','jonas']

"""correos_validos = []

for email in lista_email:
    if email:
        correos_validos.append(email)

print(correos_validos)"""

##son maneras de optimizar codigo, reducir el for en una sola linea
compresion = [correo.upper() for correo in lista_email if correo]

print(compresion)

##potenciacion, elevar su numero al cuadrado

numeros = [1,2,3,4,5,6]

potencia = [n**2 for n in numeros]
print(potencia)

##sintaxis general
## variable = 
# [expresion(que ahcer con cadaelemnto) -
#  for elemento in iterable (de donde vamos a sacar los elementos- 
# condicion (condicion opcional)]

num = [10,3,10,6,3,7,22,4,8]

pares =[n for n in num if n % 2 == 0]
print(pares)

print('------------------slicing-----------------')
#varaible[inicio:fin:salto]
##es una forma elegante de extraer partes de una secuencias, como listas, tuplas etc..
nombres= ['Jonas','beatriz','maria','jose','jesus']
print(nombres[0:-1]) #['Jonas','beatriz','maria','jose','jesus']
print(nombres[:4]) # ['Jonas', 'beatriz', 'maria', 'jose']

##sacar solo los nombres de los correos
correos2 =['Jonas@gmail.com','beatriz@gmail.com','maria@gmail.com','jose@gmail.com','jesus@gmail.com']

correos_validos= [c[:c.index('@')] for c in correos2]
print(correos_validos)

#invertir caracteres
nombre = 'Jonathan'
print(nombre[::-1])