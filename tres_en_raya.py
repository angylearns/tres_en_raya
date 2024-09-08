# 08.2.1 importamos la librería random
import random
# 09.3.1 importamos sleep de la librería time - sleep es para hacer pausas
from time import sleep


# 02. Creamos la función para pintar el tablero
def print_board(board):
    print("-------------")
    for i in range(3):
        print(f"| {board[i][0]} | {board[i][1]} | {board[i][2]} | ")
    print("-------------")


def get_layer_move(board):
    while True:
        # 04. pedir el movimiento
        move = input("Ingresa la fila y la columna (ej.: 1,1): ")

        # 04.1. como voy a recibir dos números separados por coma, los separo con split haciendo que el primera vaya a row y el segundo a column
        row, column = move.split(",")

        # 04.2. como la entrada es un string y las posiciones comienzan en 0, convierto ambas variables a int y les resto 1 a cada una
        row = int(row) - 1
        column = int(column) - 1

        # 04.3. ahora necesitamos validar que nuestros valores están en el rango del tablero; o sea, que es un movimiento válido:
        if 0 <= row < 3 and 0 <= column < 3 and board[row][column] == "-":
            return row, column
            # al hacer este ↑ return, es como si se hiciera un break. Se sale del while porque ya retorné un valor.
        else:
            print("Movimiento inválido. Inténtalo de nuevo.")


# 07. definimos la función para comprobar quién gana
def check_winner(board):
    # 07.1. validamos líneas horizontales
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-":
            return board[i][0]

    # 07.2. si no ha ganado horizontal, validamos líneas verticales
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != "-":
            return board[0][i]

    # 07.3. validamos diagonales - Como no solo puede haber dos posiciones, validamos las dos diagonales sin necesidad de bucle for
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[0][0]
    elif board[2][0] == board[1][1] == board[0][2] != "-":
        return board[2][0]

    # 07.4. si no ha ganado ninguna de las anteriores
    return None


def main():
    print("Tres en raya")

    # 01. Inicializar el tablero
    board = [["-", "-", "-"] for _ in range(3)]
    # ↑ esto es igual que esto: board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    while True:
        # 03. tras haber inicializado el tablero, lo pintamos
        print_board(board)

        # 05. obtener movimiento de la jugadora
        row, column = get_layer_move(board)
        # 06. tras haber obtenido el movimiento de la jugadora y haber validado que es correcto, le ponemos la x
        board[row][column] = "X"

        # 08. tras haber definido la función para chequear quién gana, la llamamos
        winner = check_winner(board)

        # 08.1. como en el punto 07.4 chequeamos que si winner devolvía None es porque había ganadora, si no hay ganadora, continuamos...
        if winner is not None:
            break

        # 09. ...y generamos el movimiento de la computadora con la librería random (que tenemos que importar - 08.2.1) pidiéndole que nos dé un número entero aleatorio entre 0 y 2
        computer_row = random.randint(0, 2)
        computer_column = random.randint(0, 2)

        # 09.1. entonces validamos que la posición generada no esté ocupada (!= "-") y, si lo está, le decimos que siga generando números
        while board[computer_row][computer_column] != "-" or (computer_row == row and computer_column == column):
            computer_row = random.randint(0, 2)
            computer_column = random.randint(0, 2)

        # 09.2. si la posición no está ocupada, se pinta la jugada de la computadora
        board[computer_row][computer_row] = "O"

        # 09.3. usamos sleep (que tenemos que importar - 09.3.1) para dar tiempo (1'') a que se pinte el tablero
        sleep(1)
        print_board(board)

        # 10. tras haber pintado el tablero, comprobamos si la computadora ganó
        winner = check_winner(board)

        # 10.1. y validamos si winner (que es None si hay ganadora) es distinto de None y salimos
        if winner is not None:
            break

    print_board(board)
    print(winner, "gana la partida")


if __name__ == "__main__":
    main()
