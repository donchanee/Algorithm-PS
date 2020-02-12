# https://www.acmicpc.net/problem/15651 N과 M (3)

from itertools import product
N, M = map(int, input().split())
P = product(range(1, N+1), repeat = M)
for i in P:
    print(' '.join(map(str, i)))
