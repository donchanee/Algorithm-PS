from sys import stdin
N = int(input())
L = [list(map(int, stdin.readline().split())) for x in range(N)]

for i in range(1,N):
    L[i][0] += L[i-1][0]
    for j in range(1,len(L[i])-1):
        L[i][j] = max(L[i-1][j-1], L[i-1][j]) + L[i][j]
    L[i][i] += L[i-1][i-1]

print(max(L[N-1]))
