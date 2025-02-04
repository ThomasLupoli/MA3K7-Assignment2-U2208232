import numpy as np
from itertools import product
import math

n = 4


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

def gen_winning_boards(boards):
    determinants = {}
    for board in boards:
        det = round(np.linalg.det(board))
        determinants[board.tobytes()] = det

    winning_boards = [board for board, det in determinants.items() if det == 0]
    return winning_boards


def minimax(preset_values):
    moves = np.arange(n**2)
    positions = list(preset_values.keys())
    best_move = {}

    for pos in positions:
        moves = moves[moves != n * pos[0] + pos[1]]

    for mov0 in moves:
        worst_opponent_move = []

        preset_values[(math.floor(mov0/n), mov0 % n)] = 0
        no_move = moves[moves != mov0]
        for mov1 in no_move:
            preset_values[(math.floor(mov1 / n), mov1 % n)] = 1
            boards = generate_boards(preset_values)
            winning_boards = gen_winning_boards(generate_boards(preset_values))
            worst_opponent_move.append(len(winning_boards) / len(boards))

            del preset_values[(math.floor(mov1 / n), mov1 % n)]

        best_move[(math.floor(mov0 / n), mov0 % n)] = min(worst_opponent_move)

        del preset_values[(math.floor(mov0/n), mov0 % n)]

    max_position = max(best_move, key=best_move.get)
    max_value = best_move[max_position]
    print({max_position: max_value}, "0")
    return {max_position: 0}

def op_minimax(preset_values):
    moves = np.arange(n**2)
    positions = list(preset_values.keys())
    best_move = {}

    for pos in positions:
        moves = moves[moves != n * pos[0] + pos[1]]

    for mov0 in moves:
        worst_opponent_move = []

        preset_values[(math.floor(mov0/n), mov0 % n)] = 1
        no_move = moves[moves != mov0]
        for mov1 in no_move:
            preset_values[(math.floor(mov1 / n), mov1 % n)] = 0
            boards = generate_boards(preset_values)
            winning_boards = gen_winning_boards(generate_boards(preset_values))
            worst_opponent_move.append(len(winning_boards) / len(boards))

            del preset_values[(math.floor(mov1 / n), mov1 % n)]

        best_move[(math.floor(mov0 / n), mov0 % n)] = max(worst_opponent_move)

        del preset_values[(math.floor(mov0/n), mov0 % n)]

    min_position = min(best_move, key=best_move.get)
    min_value = best_move[min_position]
    print({min_position: min_value}, "1")
    return {min_position: 1}

def best_one(preset_values):
    moves = np.arange(n ** 2)
    positions = list(preset_values.keys())
    best_move = {}

    for pos in positions:
        moves = moves[moves != n * pos[0] + pos[1]]

    for mov in moves:
        preset_values[(math.floor(mov / n), mov % n)] = 1
        boards = generate_boards(preset_values)
        winning_boards = gen_winning_boards(generate_boards(preset_values))
        best_move[(math.floor(mov / n), mov % n)] = len(winning_boards) / len(boards)
        del preset_values[(math.floor(mov / n), mov % n)]

    min_position = min(best_move, key=best_move.get)
    min_value = best_move[min_position]
    print({min_position: min_value}, "1")
    return {min_position: 1}


def game(preset_values):
    while len(preset_values) < n**2 - 1:
        if len(preset_values) % 2 == 0:
            preset_values.update(op_minimax(preset_values))
        else:
            preset_values.update(minimax(preset_values))
    return generate_boards(preset_values)


for m in game({}):
    for row in m:
       print(row)
    print()

# print("this:", len(gen_winning_boards(generate_boards({(0, 0): 0, (1, 1): 1, (2, 2): 1}))) / len(generate_boards({(0, 0): 0, (1, 1): 1, (2, 2): 1})))
