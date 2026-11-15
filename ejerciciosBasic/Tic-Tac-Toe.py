"""
Escenario

Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. 
Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

- la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
- el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
- el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
- todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
- el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, 
    por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
- el programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continua, 
    el juego termina en empate, tu ganas, o la maquina gana;
- la maquina responde con su movimiento y se verifica el estado del juego;
- no se debe implementar algún tipo de inteligencia artificial - la maquina elegirá un cuadro de manera aleatoria,
     eso es suficiente para este juego.
"""


import random

def crear_tablero():
    return [" "] * 9

def mostrar_tablero(tablero):
    print("\n")
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]}      1 | 2 | 3")
    print("---+---+---    ---+---+---")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]}      4 | 5 | 6")
    print("---+---+---    ---+---+---")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]}      7 | 8 | 9")
    print("\n")

def verificar_ganador(tablero, ficha):
    combinaciones = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columnas
        [0, 4, 8], [2, 4, 6]              # diagonales
    ]
    for combo in combinaciones:
        if all(tablero[i] == ficha for i in combo):
            return True
    return False

def tablero_lleno(tablero):
    return " " not in tablero

def movimiento_maquina(tablero):
    casillas_libres = [i for i, v in enumerate(tablero) if v == " "]
    return random.choice(casillas_libres)

def pedir_movimiento_usuario(tablero):
    while True:
        try:
            casilla = int(input("Tu turno (O) - Elige una casilla (1-9): "))
            if casilla < 1 or casilla > 9:
                print("Error: El número debe estar entre 1 y 9.")
            elif tablero[casilla - 1] != " ":
                print("Error: Esa casilla ya está ocupada.")
            else:
                return casilla - 1
        except ValueError:
            print("Error: Debes ingresar un número entero.")

def jugar():
    print("=" * 40)
    print("     BIENVENIDO AL TIC-TAC-TOE")
    print("  Máquina = X  |  Tú = O")
    print("=" * 40)

    tablero = crear_tablero()

    # La máquina siempre empieza en el centro (casilla 5, índice 4)
    tablero[4] = "X"
    print("\nLa máquina coloca su X en el centro (casilla 5).")
    mostrar_tablero(tablero)

    while True:
        # Turno del usuario
        indice = pedir_movimiento_usuario(tablero)
        tablero[indice] = "O"
        mostrar_tablero(tablero)

        if verificar_ganador(tablero, "O"):
            print("¡Felicidades! ¡Ganaste! 🎉")
            break

        if tablero_lleno(tablero):
            print("¡Empate! Nadie gana.")
            break

        # Turno de la máquina
        indice_maquina = movimiento_maquina(tablero)
        tablero[indice_maquina] = "X"
        print(f"La máquina coloca su X en la casilla {indice_maquina + 1}.")
        mostrar_tablero(tablero)

        if verificar_ganador(tablero, "X"):
            print("La máquina gana. ¡Mejor suerte la próxima vez!")
            break

        if tablero_lleno(tablero):
            print("¡Empate! Nadie gana.")
            break

    print("\n¡Gracias por jugar!")

if __name__ == "__main__":
    jugar()