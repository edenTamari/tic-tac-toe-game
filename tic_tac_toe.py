"""
@Description : Implementation of the Tic-Tac-Toe game
@Author: Eden Tamari
"""
import random

"""
        The function returns empty board game

        @Param:
                size (int): The size of the board
        @Returns:
                 list[list[str]]
"""
def create_board(size=3):
    return [[' ' for _ in range(size)] for _ in range(size)]


"""
        The function prints the board game

        @Param:
                board (list[list[str]]): the board game
        @Returns:
                void
"""
def print_board(board):
    board_to_print = ''
    counter = 0
    for row in board:
        for item in row:
            board_to_print += '[' + item + ']'
        if counter != len(board) - 1:
            board_to_print += '\n'
        counter += 1
    print(board_to_print)


"""
        The function randomly chooses which player starts the game

        @Returns:
                int
"""
def which_player_start():
    return random.randint(1, 2)


"""
         The function returns the player whose turn it is to play now

        @Param:
                player (int): the current player
        @Returns:
                string
"""
def next_turn(player):
    return 2 // player


"""
        The function puts the player symbol in the given location

        @Param:
                board (list[list[str]]): the board game
                player (int): the current player
                row (int): the row number in the board
                col (int): the col number in the board
        @Returns:
                board (list[list[str]]): the board game
"""
def move(board, player, row, col):
    if player == 1:
        sign = 'X'
    else:
        sign = 'O'
    if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0:
        raise IndexError(print('Invalid row or col value'))
    elif board[row][col] != ' ':
        raise TypeError(print('This cell is already taken!'))
    else:
        board[row][col] = sign
        return board


"""
        The function checks if there is a sequence of the same symbol in the same row

        @Param:
                board (list[list[str]]): the board game
                player (int): the current player
        @Returns:
                boolean
"""
def win_in_row(board, player):
    row_x = ['X'] * len(board)
    row_o = ['O'] * len(board)
    if player == 1:
        for row in board:
            if row == row_x:
                return True
    if player == 2:
        for row in board:
            if row == row_o:
                return True
    return False


"""
        The function checks if there is a sequence of the same symbol in the same col

        @Param:
                board (list[list[str]]): the board game
                player (int): the current player
        @Returns:
                boolean
"""
def win_in_col(board, player):
    col_x = ['X'] * len(board)
    col_o = ['O'] * len(board)
    for col in range(len(board)):
        temp_col = []
        for row in board:
            temp_col.append(row[col])
        if temp_col == col_x and player == 1:
            return True
        if temp_col == col_o and player == 2:
            return True
    return False


"""
        The function checks if there is a sequence of the same symbol in one of the diagonals

        @Param:
                board (list[list[str]]): the board game
                player (int): the current player
        @Returns:
                boolean
    """
def win_in_diagonal(board, player):
    size = len(board)
    dia_x = ['X'] * len(board)
    dia_o = ['O'] * len(board)
    main_dia = []
    second_dia = []
    row = 0
    col = 0
    while row < size:
        main_dia.append(board[row][col])
        row += 1
        col += 1

    row = 0
    col = size-1
    while row < size:
        second_dia.append(board[row][col])
        row += 1
        col -= 1

    if player == 1:
        if main_dia == dia_x or second_dia == dia_x:
            return True
    if player == 2:
        if main_dia == dia_o or second_dia == dia_o:
            return True
    return False


"""
        The function checks if board is full

        @Param:
                board (list[list[str]]): the board game
        @Returns:
                boolean
"""
def board_is_full(board):
    for row in board:
        for item in row:
            if item == ' ':
                return False
    print('It\'s a tie!')
    return True


"""
        The function checks if the current player won

        @Param:
                board (list[list[str]]): the board game
                player (int): the current player
        @Returns:
                boolean
"""
def win_game(board, player):
    if win_in_row(board, player) or win_in_col(board, player) or win_in_diagonal(board, player):
        return True
    return False


"""
        Implementation of the game logic

        @Returns:
                void
"""
def start_game():
    size = int(input("Enter board size (3 for classic 3x3, or larger): "))
    if size < 3:
        board = create_board()
    else:
        board = create_board(size)
    current_player = which_player_start()
    while not board_is_full(board):
        if current_player == 1:
            sign = 'X'
        else:
            sign = 'O'
        print_board(board)
        print('Go on player', sign, 'it\'s your turn!')
        row = int(input('Enter row position (start from 0): '))
        col = int(input('Enter column position (start from 0): '))
        try:
            move(board, current_player, row, col)
        except:
            continue
        else:
            if win_game(board, current_player):
                print_board(board)
                print(sign, 'wins!')
                with open("fireworks_ascii_art.txt", "r", encoding="utf-8") as fireworks_ascii_art:
                    FIREWORKS = fireworks_ascii_art.read()
                print(FIREWORKS)

                return
            else:
                current_player = next_turn(current_player)


start_game()