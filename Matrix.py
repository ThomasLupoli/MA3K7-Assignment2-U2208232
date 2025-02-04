import matplotlib.pyplot as plt
import numpy as np
from random import randint
import math

n = 6
moves = np.arange(n**2)
A = np.zeros(n**2).reshape(n, n)
my_go = True



while moves.size > 0:
    place = randint(0, moves.size - 1)
    num = moves[place]
    moves = np.delete(moves, place, 0)
    i = math.floor(num/n)
    j = num % n
    if my_go:
        A[i, j] = 0
    else:
        A[i, j] = 1
    my_go = not my_go


det = round(np.linalg.det(A))

print(round(det))
