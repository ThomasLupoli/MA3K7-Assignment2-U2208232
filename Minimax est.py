import numpy as np
from random import randint
from itertools import product
import math

n = 3


def gen_winning_boards(preset_values):
    positions = list(preset_values.keys())
    A = np.zeros(n**2).reshape(n, n)
    moves = np.arange(n**2)
    best_move = {}

    for pos in positions:
        A[pos[0], pos[1]] = preset_values[pos]
        moves = moves[moves != n * pos[0] + pos[1]]

    total = 1000
    for mov0 in moves:
        worst_opponent = []
        no_move = moves[moves != mov0]
        A[math.floor(mov0 / n), mov0 % n] = 0
        for mov1 in no_move:
            A[math.floor(mov1/n), mov1 % n] = 1
            wins = 0
            no_moves = no_move[no_move != mov1]
            for k in range(total):
                AA = A
                movess = no_moves
                my_go = True

                while movess.size > 0:
                    place = randint(0, movess.size - 1)
                    num = movess[place]
                    movess = np.delete(movess, place, 0)
                    i = math.floor(num/n)
                    j = num % n
                    if my_go:
                        AA[i, j] = 0
                    else:
                        AA[i, j] = 1
                    my_go = not my_go

                if round(np.linalg.det(A)) == 0:
                    wins += 1

            worst_opponent.append(wins / total)
        best_move[(math.floor(mov0 / n), mov0 % n)] = min(worst_opponent)

    max_position = max(best_move, key=best_move.get)
    max_value = best_move[max_position]
    print({max_position: max_value}, "0")
    return {max_position: 0}


def op_gen_winning_boards(preset_values):
    positions = list(preset_values.keys())
    A = np.zeros(n**2).reshape(n, n)
    moves = np.arange(n**2)
    best_move = {}

    for pos in positions:
        A[pos[0], pos[1]] = preset_values[pos]
        moves = moves[moves != n * pos[0] + pos[1]]

    total = 1000
    for mov0 in moves:
        worst_opponent = []
        no_move = moves[moves != mov0]
        A[math.floor(mov0 / n), mov0 % n] = 1
        for mov1 in no_move:
            A[math.floor(mov1/n), mov1 % n] = 0
            wins = 0
            no_moves = no_move[no_move != mov1]
            for k in range(total):
                AA = A
                movess = no_moves
                my_go = False

                while movess.size > 0:
                    place = randint(0, movess.size - 1)
                    num = movess[place]
                    movess = np.delete(movess, place, 0)
                    i = math.floor(num/n)
                    j = num % n
                    if my_go:
                        AA[i, j] = 0
                    else:
                        AA[i, j] = 1
                    my_go = not my_go

                if round(np.linalg.det(A)) == 0:
                    wins += 1

            worst_opponent.append(wins / total)
        best_move[(math.floor(mov0 / n), mov0 % n)] = max(worst_opponent)

    min_position = min(best_move, key=best_move.get)
    min_value = best_move[min_position]
    print({min_position: min_value}, "1")
    return {min_position: 1}


def generate_boards(preset_values):
    all_positions = [(i, j) for i in range(n) for j in range(n)]

    free_positions = [pos for pos in all_positions if pos not in preset_values]

    all_boards = []
    for values in product([0, 1], repeat=len(free_positions)):
        matrix = np.zeros((n, n), dtype=int)

        for (i, j), val in preset_values.items():
            matrix[i, j] = val

        for (pos, val) in zip(free_positions, values):
            matrix[pos] = val

        all_boards.append(matrix)

    legit_boards = []
    for board in all_boards:
        if np.bincount(board.flatten())[1] == math.ceil(n ** 2 / 2):
            legit_boards.append(board)
    return legit_boards



def game(preset_values):
    while len(preset_values) < n**2 - 1:
        if len(preset_values) % 2 == 0:
            preset_values.update(op_gen_winning_boards(preset_values))
        else:
            preset_values.update(gen_winning_boards(preset_values))
    return generate_boards(preset_values)


for m in game({}):
    for row in m:
        print(row)
    print()
