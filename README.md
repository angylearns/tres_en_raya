# Tres en Raya

Este repositorio contiene una implementación sencilla del popular juego de **Tres en Raya** en Python. El proyecto es parte de una actividad del [Bootcamp de Introducción a la Programación](https://codigofacilito.com/programas/introduccion-programacion-g5?play=true) de **Código Facilito**.

## Descripción

El juego de **Tres en Raya** (también conocido como Tic-Tac-Toe) es jugado en un tablero de 3x3, donde dos jugadores, la persona usuaria y la computadora, toman turnos para colocar su símbolo (`X` o `O`) en una de las casillas del tablero. El objetivo es conseguir tres símbolos iguales en fila, columna o diagonal antes que el oponente.

En esta implementación:
- La persona usuaria juega como `X`.
- La computadora juega como `O`, pero su estrategia está basada únicamente en la generación de movimientos aleatorios, por lo que **las probabilidades de que gane son bajas**.

## Estructura del código

1. **Inicialización del tablero**:
   Se crea un tablero de 3x3 representado por una lista de listas, donde inicialmente todas las posiciones están vacías y representadas por el símbolo `-`.

   ```python
   board = [["-", "-", "-"] for _ in range(3)]
   ```

2. **Función `print_board(board)`**:
   Esta función imprime el tablero en la consola de manera estructurada.

3. **Función `get_layer_move(board)`**:
   Esta función solicita al usuario su jugada en formato "fila,columna" y se encarga de validar que la entrada sea válida (dentro del rango del tablero y en una casilla vacía).

4. **Función `check_winner(board)`**:
   Esta función revisa si alguna de las jugadoras ha ganado verificando:
   - Filas.
   - Columnas.
   - Diagonales.

5. **Lógica del juego**:
   El juego alterna entre la persona usuaria y la computadora hasta que hay una ganadora o el tablero se llena. La computadora selecciona su movimiento de manera aleatoria usando la función `randint` del módulo `random`.

6. **Turno de la computadora**:
   La computadora genera su movimiento con números aleatorios hasta que encuentra una posición válida en el tablero. Dado que su lógica es completamente aleatoria, **las probabilidades de que gane son bajas**.

   ```python
   computer_row = random.randint(0, 2)
   computer_column = random.randint(0, 2)
   ```

7. **Uso de `sleep(1)`**:
   Se utiliza la función `sleep` del módulo `time` para pausar el juego por 1 segundo después de cada jugada de la computadora, lo que mejora la experiencia visual.

## Instalación y Ejecución

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/angylearns/tres_en_raya.git
   cd tres_en_raya
   ```

2. Asegúrate de tener Python instalado en tu máquina.

3. Ejecuta el juego:
   ```bash
   python tres_en_raya.py
   ```

## Instrucciones para Jugar

1. Se mostrará el tablero vacío y se te pedirá ingresar tu jugada en el formato "fila,columna". Por ejemplo, para seleccionar la casilla en la esquina superior izquierda, ingresa `1,1`.
   
2. La computadora seleccionará su jugada de manera aleatoria después de que completes tu turno.

3. El juego termina cuando una de las jugadoras consiga alinear tres símbolos (`X` o `O`) de forma horizontal, vertical o diagonal.

## Consideraciones

- La **computadora no tiene una estrategia** predefinida, su jugada se basa únicamente en la generación de números aleatorios. Esto significa que la probabilidad de que gane es baja.
- El juego no detecta empates en su estado actual, pero esto podría ser una buena mejora futura.

## Mejoras Futuras

Algunas posibles mejoras que se pueden implementar en este juego son:
- Detectar empates cuando todas las casillas están llenas y no hay ganadora.
- Implementar una estrategia más inteligente para la computadora (minimax, por ejemplo).
- Agregar una interfaz gráfica para mejorar la experiencia de usuario.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o deseas agregar una mejora, no dudes en abrir un issue o enviar un pull request.
