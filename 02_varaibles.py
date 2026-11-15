#variables: una referencia que apunta a un objeto en memoria
#es ulugar en memoria para almacenar cualkquier tipo de dato y el valor de ese datos
# podria variar en un futuro(en teoria es encapsular datos)
miVarieble = 'Jonathan' #string
print(miVarieble)
num = 1 + 3 #numerico
num2 = num + 2 #numerico
print(num2)
bloneano = True # booleano

"""cuando una variable cambia de """

num3 = 23;
numero_a_texto = str(num3)
print(type(numero_a_texto))
print(numero_a_texto)

#funcion len (busca la longitud de una cadena de texto)
print(len(miVarieble))

nombre2 = 'jonathan';
apellido = 'montes'; 
edad = '23';

#concatenado
print('mi nombre es ' + nombre2 + ' ' + apellido + ' y tengo ' + edad + ' años' )
#soliciar datos a un usuario
donde = input('de donde eres: ')
print(donde)
#input
nombre = input('como te llamas: ')
edad2 = input ('cuantos años tienes: ')
print(nombre + ' ' + 'tiene ' + edad2 + ' años de edad')

print('hola mundo')

###variables


# Enteros (int) → números sin decimal
edad = 28
años_experiencia = 3

# Flotantes (float) → números con decimal
altura = 1.75
salario_mensual = 45000.50

# Strings (str) → texto
nombre = "jonathan"
lenguaje_favorito = 'Python'  # comillas simples o dobles, da igual

# Booleanos (bool) → Verdadero o Falso
es_data_engineer = True
esta_estudiando = True

print(nombre, "tiene", edad, "años y gana $", salario_mensual)

##declaro variables con el tipo de datpo
novia: str= 'dayana' 
edad: int = 19

print('################### METODOS ###############')

data1 = 'Jonathan Montes'
data2 = data1.upper()
print(data2)
amigo = 'JONAS'
result = amigo.lower()
print(result)
saludo = '        hola     '
print(saludo.strip())
correo = 'jona@gmail.com'
print(correo.split('@'))

print(f'hola mi correo es {correo.upper()}')
