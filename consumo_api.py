## primero necessito el modulo que me permita conectar a esa API

import requests 

# se crea una varaible
response = requests.get('https://jsonplaceholder.typicode.com/users')
#se debe convertir el resultado a json
users = response.json()

for user in users:
    nombre = user['name']
    correo = user['email']
    print(f'Hola {nombre}, su correo es {correo}')
    print('--------')