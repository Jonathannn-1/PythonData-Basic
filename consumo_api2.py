import requests
import json

url = 'https://pokeapi.co/api/v2/pokemon?limit=10'

respuesta = requests.get(url)

result = respuesta.json()

pokemon_nombres= []

for pokemon in result['results']:
    nombre = pokemon['name']
    pokemon_nombres.append(nombre)
    
print(pokemon_nombres)
    

