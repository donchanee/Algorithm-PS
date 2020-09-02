from sys import stdin
N = int(input())
L = [list(map(int, stdin.readline().split())) for x in range(N)]

for i in range(1,N):
    L[i][0] = min(L[i-1][1], L[i-1][2]) + L[i][0]
    L[i][1] = min(L[i-1][0], L[i-1][2]) + L[i][1]
    L[i][2] = min(L[i-1][1], L[i-1][0]) + L[i][2]

print(min(L[N-1]))

# DP 미리 선 배열 만들어 놓는거 말고 다음 행에서 이전 행으로 가는 방법
