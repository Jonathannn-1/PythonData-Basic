"""Lección 3.1 – Listas: creación, indexación, slicing y métodos principales

Las listas son mutables, ordenadas y permiten duplicados. Son el tipo más usado al inicio."""

# Creación
# el codigo se define de la manera más simple 
# asignas un valor de una variable y defines la lista, 
# la lista puede contener diversos tipos de valores.
frutas = ["manzana", "banana", "naranja", "kiwi"]
numeros = [10, 5, 8, 3, 12]
mezcla = [1, "hola", True, 3.14]

# Indexación (0-based) y negativa (desde el final)
print(frutas[0])      # manzana
print(frutas[-1])     # kiwi (último elemento)
print(frutas[1:3])    # ['banana', 'naranja']  → slicing [inicio:fin] fin no incluido

# Slicing avanzado
print(frutas[::2])    # cada 2 → ['manzana', 'naranja']
print(frutas[::-1])   # reversa → ['kiwi', 'naranja', 'banana', 'manzana']

# Métodos principales
frutas.append("pera")          # agrega al final
frutas.extend(["mango", "uva"]) # agrega varios
frutas.insert(1, "fresa")      # inserta en posición
frutas.pop()                   # quita y retorna el último
frutas.remove("banana")        # quita el primero que encuentre
frutas.sort()                  # ordena alfabéticamente (in-place)
print(sorted(frutas))          # versión que retorna nueva lista

print(len(frutas))             # cuántos elementos
print("pera" in frutas)        # True / False

"""Lección 3.2 – Tuplas: inmutables y unpackingTuplas = listas que no se pueden modificar.
 Útiles para datos fijos (coordenadas, claves de config, retornos múltiples)."""


# Creación (paréntesis opcionales)
coordenadas = (19.4326, -99.1332)  # lat, lon CDMX
persona = "kalex", 28, "Data Engineer"  # sin paréntesis también es tupla

# Unpacking (desempaquetado)
nombre, edad, rol = persona
print(f"{nombre} ({edad} años) → {rol}")

lat, lon = coordenadas
print(f"Lat: {lat}, Lon: {lon}")

# Útil en funciones que retornan varios valores
def obtener_info():
    return "Python", 3.13, "2026"

lenguaje, version, año = obtener_info()


"""Lección 3.3 – Sets: conjuntos sin duplicados y sin ordenIdeales para eliminar duplicados,
membresía rápida y operaciones matemáticas de conjuntos."""

# Creación
lenguajes = {"Python", "SQL", "Airflow", "Python"}  # duplicado se elimina
print(lenguajes)  # {'Python', 'SQL', 'Airflow'}

# Operaciones
otros = {"Spark", "DBT", "Python", "Kafka"}

union = lenguajes | otros                  # o lenguajes.union(otros)
interseccion = lenguajes & otros           # o .intersection()
diferencia = lenguajes - otros             # o .difference()
diferencia_simetrica = lenguajes ^ otros   # o .symmetric_difference()

print(f"Intersección: {interseccion}")
print(f"¿Python está? {'Python' in lenguajes}")  # muy rápido en sets


"""Lección 3.4 – Diccionarios: keys/values y métodos útilesLos dicts son la estructura 
estrella para datos estructurados (JSON-like)."""

# Creación
perfil = {
    "nombre": "kalex",
    "edad": 28,
    "rol": "Data Engineer",
    "skills": ["Python", "SQL", "Airflow", "DBT"],
    "salario_anual": 65000
}

# Acceso
print(perfil["nombre"])
print(perfil.get("ciudad", "No especificada"))  # seguro, no KeyError

# Métodos
print(perfil.keys())     # todas las claves
print(perfil.values())   # todos los valores
print(perfil.items())    # lista de tuplas (clave, valor)

perfil["ciudad"] = "CDMX"               # agregar / actualizar
perfil.pop("salario_anual")             # eliminar
del perfil["edad"]                      # otra forma de eliminar

# Iterar
for clave, valor in perfil.items():
    print(f"{clave.capitalize()}: {valor}")

"""Lección 3.5 – List comprehensions y dict comprehensions (la joya de Python)
Forma concisa y legible de crear listas/dicts filtrando/transformando."""

# List comprehension básica
cuadrados = [x**2 for x in range(1, 11)]          # [1, 4, 9, ..., 100]

# Con condición
pares = [x for x in range(20) if x % 2 == 0]      # [0, 2, 4, ..., 18]

# Transformación + filtro
nombres = ["ana", "juan", "karla", "pedro"]
mayusculas_largas = [n.upper() for n in nombres if len(n) > 3]
# ['JUAN', 'KARLA', 'PEDRO']

# Dict comprehension
cuadrados_dict = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Conteo de palabras simple
frase = "python es genial python es poderoso"
conteo = {palabra: frase.split().count(palabra) for palabra in set(frase.split())}


##ejercicios:

print('------------------------------------------EJERCICIOS--------------------------------')

"""Filtrar listas
Dada numeros = [4, 12, 7, 19, 3, 25, 8], crea una nueva lista solo con números > 10 usando list comprehension."""

numeros = [4, 12, 7, 19, 3, 25, 8]

#lista de comprension con if-else 
numMayores = [x if x > 10 else '-' for x in numeros ]
print(numMayores)

#lista de comprension con if
lista3 = [(z*z) for z in numeros if z > 10]
print(lista3)


"""num_cuadrado = [(i*i) for i in range(1,11)]
print(num_cuadrado)"""

"""Contar palabras
Pide una frase al usuario y muestra cuántas veces aparece cada palabra (usa dict + split())."""

frase1 = input('Ingrese una Frase: ')

##compresion de diccionarios

conteoPalabras = {palabra: frase1.split().count(palabra) for palabra in set(frase1.split())}
print(conteoPalabras)

"""Eliminar duplicados
Dada una lista con duplicados, conviértela a lista sin duplicados manteniendo orden
 (usa dict.fromkeys() o set + list)."""

colores = ['rojo', 'rojo', 'amarillo', 'verde', 'amarillo', 'azul']
colores_unicos = [j for j in list(set(colores))]

print(colores_unicos)


