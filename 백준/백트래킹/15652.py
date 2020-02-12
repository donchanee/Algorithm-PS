# https://www.acmicpc.net/problem/15652 N과 M (4) 

from itertools import combinations_with_replacement
N, M = map(int, input().split())
P = combinations_with_replacement(range(1, N+1), M)
for i in P:
    print(' '.join(map(str, i)))
