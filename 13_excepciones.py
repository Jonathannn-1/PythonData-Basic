#corresponde al manejo de errores#

numero_1 = 2
numero_2 = 4
numero_1 = '1'

try:
    print(numero_1 + numero_2)
    print('se ejecuto el programa')
except:
    print('Ocurrio un error')
else:
    print('continua la ejecucion')
finally:
    print('ejecucion finalizada')

#excepcionmes por tipo

num = 2
num2 = 3
num = '2'

try:
    print(num + num2)
    print('se ejecuto por tipo de excepcion')
except TypeError:
    print('error de typeError')
except ValueError:
    print('error de valueError')

##errores definidos al usuario
try:
    print(num + num2)
    print('se ejecuto por tipo de excepcion')
except ValueError as error:
    print(error)


