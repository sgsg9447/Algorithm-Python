from itertools import permutations, combinations

# li = [1,2,3]
# pers1 = list(permutations(li,2))
# pers2 = list(combinations(li,2))

# print(pers1)
# print('----------------------------------------------')
# print(pers2)

import sys

N = int(sys.stdin.readline())

clues = []
for _ in range(N):
    inputs = list(map(int, sys.stdin.readline().split()))
    clues.append(inputs)