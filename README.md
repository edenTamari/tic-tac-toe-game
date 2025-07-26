### Tic-Tac-Toe Game (Python CLI)

A simple two-player **Tic-Tac-Toe** (a.k.a. X-O) game implemented in Python.  
Players alternate turns on a square board of any size (3x3 or larger) until someone wins or the game ends in a draw.

### How to Play

- Choose the board size at the beginning (e.g., 3 for classic Tic-Tac-Toe).
- Players `X` and `O` take turns entering the row and column where they want to place their symbol.
- A player wins by aligning their symbols in a row, column, or diagonal.
- If the board is full with no winner, the game ends in a draw.

### Features

- Dynamic board size (3x3 and larger)
- Input validation and clear error messages
- Winner and draw detection
- Turn-based CLI interaction

#### Example Input

```text
Enter board size (3 for classic 3x3, or larger): 3

Current Board:
   0   1   2
0    |   |  
  -----------
1    |   |  
  -----------
2    |   |  

Player X's turn
Enter row (0 to 2): 0
Enter column (0 to 2): 0
