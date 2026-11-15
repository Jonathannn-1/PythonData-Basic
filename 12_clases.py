##
# CLASES 
# SIRVE PARA AGRUPAR UNA LOGICA EN CONCRETO#


##definienco una clase: def es un constructor de clases: el INT define el constructor
## self se iguala al valor mismo
class Persona: 
    def __init__(self,nombre, apellido,novia = 'dayana', alias = 'jona'):
        self.nombre = nombre
        self.apellido = apellido
        self.alias = alias
        self.__novia = novia #propíedad privada

    ##metodos
    def hablar(self):
        print('Hola, como estas?')
    
    def correr(self):
        print(f'{self.nombre} corre por las mañanas')

    ##alias definofo por el programador
    def aliasP (self):
        print(f'su alias es ({self.alias})')
    
    def get_novia (self):
        return self.__novia

persona1 = Persona('Jonathan','montes');
print(f'{persona1.nombre} {persona1.apellido}')
persona1.hablar()
persona1.correr()
persona1.aliasP()
persona1.nombre= 'jonathan Antonio' ## cambiando valor del argumento nombre
persona1.apellido= 'Montes suarez'
print(f'{persona1.nombre} {persona1.apellido}')##impresion modificada

print(persona1.get_novia())##no se imprime el valor