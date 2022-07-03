#!/usr/bin/env python
import sys

def rowx(x):
    return [3*x, 3*x+1, 3*x+2]

def coly(y):
    return [0+y, 3+y, 6+y]

diagdown = [0, 4, 8]
diagup = [2, 4, 6]
rows = [rowx(i) for i in range(3)]
cols = [coly(i) for i in range(3)]
diags = [diagdown, diagup]
all_directions = rows + cols + diags

def possible(board):
    return [i for i, x in enumerate(board) if x == " "]

def display_possible(board):
    return ", ".join(str(x) for x in possible(board))

def player(board):
    return (board.count(" ")-1) % 2

def display_player(p):
    return "X" if p else "O"

def moves_left(board):
    return board.count(" ")

def winner(board):
    if moves_left(board) < 5:
        for direction in all_directions:
            try:
                if sum(int(board[i]) for i in direction) == 3:
                    return "X"
                if sum(int(board[i]) for i in direction) == 0:
                    return "O"
            except ValueError:
                continue
        if moves_left(board) == 0:
            return "nobody"
    return False

def display_cell(x):
    if x == "1":
        return "X"
    if x == "0":
        return "O"
    return x

def display(board):
    print()
    print(
        "\n_ _ _\n".join(
            "|".join(display_cell(board[3*x+y]) for y in range(3))
            for x in range(3)
        )
    )
    print()

def new_board(board, move):
    return board[:move] + str(int(player(board))) + board[move+1:]

def get_human_player():
    while True:
        x = input("Would you like to be noughts O or crosses X?: ")
        if x.lower() == "x":
            return True
        return False

def human_move(board):
    while True:
        try:
            move = input(f"Choose a move from {display_possible(board)}: ")
            if int(move) in possible(board):
                return new_board(board, int(move))
            print("That number was not valid, please choose another.")
        except (ValueError, TypeError):
            print("Please input a number, not a string.")

def score(result):
    if result == "O":
        return 1
    if result == "X":
        return -1
    return 0

def maxmin(x, maximise):
    return max(x) if maximise else min(x)

def minimax(board, maximise=True):
    if result:=winner(board):
        return score(result)
    return maxmin(
        [
            minimax(new_board(board, move), not maximise)
            for move in possible(board)
        ],
        maximise
    )

def computer_best_move(board):
    best_minimax_score = None
    best_move = None
    for move in possible(board):
        minimax_score = minimax(new_board(board, move), maximise=player(board))
        if (
                best_move is None or
                (player(board) and minimax_score < best_minimax_score) or
                (not player(board) and minimax_score > best_minimax_score)
        ):
            best_minimax_score = minimax_score
            best_move = move
    return best_move

def computer_move(board):
    move = computer_best_move(board)
    return new_board(board, move)

def main(human=False):
    try:
        board = " "*9
        while not winner(board):
            display(board)
            if player(board) == human:
                board = human_move(board)
            else:
                board = computer_move(board)
        display(board)
        print(f"Finished! Winner is {winner(board)}")
    except (EOFError, KeyboardInterrupt):
        print("\nAbort\n")
        sys.exit()

if __name__=="__main__":
    HUMAN = get_human_player()
    main(human=HUMAN)
