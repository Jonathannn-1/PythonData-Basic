## modulos: para llamar los mldulos no deben tener caracteres especiales en sus ficheros 

## importanos el modulo completo
import module
##aqui accedemos a una funcion en especifico e incluso el valor de la funcion
from module import valor, suma 
import math

## importacion de mis funciones
module.suma(10,79)


print(suma(23,459))
valor('hola amor')

## usando el modulo math
print(math.pi)
#potenciacion
print(math.pow(2,4))

try:
    value = input("Ingresa un valor: ")
    print(value/value)
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada errónea...")
except TypeError:
    print("Entrada muy errónea...")
except:
    print("¡Buuu!")


















































