
print('hola')

#string 

nombre, edad = 'jona', 23;
#formatear las varaibles con las llaves sirve para llamar el valor en ccrudo
print('hola mi nombre es {} y tengo {} años'.format(nombre,edad))
#esto tambien se puede hacer con el signo mas "+"

print('hola mi nombre es %s y tengo %s años' %(nombre, edad))
print(f'hola mi nombre es {nombre} y tengo {edad} años');

#------------------------------------------metodo 
# #slice (saca caracteres por particiones, donde lka primera letra es 0, la segunda es 1
#tercera es la segunda y asi sucesicamente)
lenguaje = 'python'

slice_lengue = lenguaje[1:3]
print(slice_lengue)

##reverse
reverse_lengu = lenguaje[::1-2]

#---------------------------------------funciones

print(lenguaje.capitalize())#pone la primera letra en mayusculas
print(lenguaje.upper())#PONE TODAS LAS LETRAS EN MAYUSCULAS
print(lenguaje.count("p"))#numero de caracteres que se le pase compo parametro
print(lenguaje.lower())#las llama todas minisculas
print(lenguaje.isnumeric())#valida si es un numero
print(lenguaje.startswith('p'))#valida si el texto empieza por x letra