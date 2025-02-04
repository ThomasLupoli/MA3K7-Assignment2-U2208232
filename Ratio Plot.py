import matplotlib.pyplot as plt
import numpy as np
from random import randint
import math

total = 10000
n_total = 20
wins = np.zeros(n_total)

n = np.arange(n_total) + 1

for p in range(n_total):
    for k in range(total):
        moves = np.arange(n[p]**2)
        A = np.zeros(n[p]**2).reshape(n[p], n[p])
        my_go = False

        while moves.size > 0:
            place = randint(0, moves.size - 1)
            num = moves[place]
            moves = np.delete(moves, place, 0)
            i = math.floor(num/n[p])
            j = num % n[p]
            if my_go:
                A[i, j] = 0
            else:
                A[i, j] = 1
            my_go = not my_go

        if round(np.linalg.det(A)) == 0:
            wins[p] += 1

print(wins / total)

fig, ax = plt.subplots(figsize=(8, 5), dpi=100)


ax.plot(n, wins / total, marker='o', linestyle='-', color='royalblue', markersize=8, linewidth=2)


ax.set_xlabel('n = ', fontsize=12, fontweight='bold')
ax.set_ylabel('Ratio', fontsize=12, fontweight='bold')
ax.set_title('Ratio of Winning Boards of size n', fontsize=14, fontweight='bold')


ax.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)
ax.set_xticks(n)


ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)


plt.show()
