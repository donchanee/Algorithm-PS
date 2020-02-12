# https://www.acmicpc.net/problem/15650 N과 M (2) 

from itertools import combinations
N, M = map(int, input().split())
P = combinations(range(1, N+1), M)
for i in P:
    print(' '.join(map(str, i)))
