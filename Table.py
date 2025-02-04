import numpy as np
from itertools import product
import math

n = 3
all_boards = list(product([0, 1], repeat=n**2))
good_boards = []
for board in all_boards:
    if board.count(0) == math.ceil(n**2 / 2):
        good_boards.append(board)

determinants = {}
for board in good_boards:
    matrix = np.array(board).reshape(n, n)
    det = round(np.linalg.det(matrix))
    determinants[board] = det

winning_boards = [board for board, det in determinants.items() if det == 0]

print("Total Winning Boards:", len(winning_boards))


