####  mini proyecto:  Gestor de contactos simple (CRUD)
## 1. agregar, buscar,listar y eliminar
## crear un menu que le permita al usuario elegir opciones

contactos = {}

def agregar():
    nombre = input('Ingresa el nombre:').strip().title()
    telefono = input('Ingrese su telefono:').strip()
    if nombre in contactos:
        print('Ya existe el contacto...')
    contactos[nombre] = telefono
    print(f'{nombre} {telefono} contacto creado/actualizado')

def buscar():
    nombre = input('Nombre del contacto:').strip().title()
    telefono = contactos.get(nombre,'contacto no encontrado' )
    print(f'{nombre} {telefono}')

def listar():
    if not contactos:
        print('No hay contactos que enlistar')
        return
    for idx, (nombre, tel) in enumerate(sorted(contactos.items()),1):
        print(f'{idx} {nombre:.<20} {tel}')

def eliminar():
    nombre = input('Ingrese el contacto a elminar: ').strip().title()
    if nombre in contactos:
        del contactos[nombre]
        print(f'{nombre} eliminado')
    else:
        print('No se encontro')


def menu():
    while True:

        print('\n----- Gestor de contactos ------')
        print('1. Agregar/actualizar')
        print('2. Buscar')
        print('3. Listar todos')
        print('4. Eliminar')
        print('5. Salir')

        opcion = input('Ingrese una ipción (1-5): ')

        if opcion == '1':
            agregar()
        elif opcion == '2':
            buscar()
        elif opcion == '3':
            listar()
        elif opcion == '4':
            eliminar()
        elif opcion == '5':
            print('Adios, ya tus conttactos se guardaron en un lgar en memoria')
            break
        else:
            print('Opción invalida')

##iniciar programa

if __name__ == '__main__':
    menu()