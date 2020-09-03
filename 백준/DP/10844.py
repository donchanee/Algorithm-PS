N = int(input())
L = [[0] * 10 for _ in range(N+1)]

for i in range(1,10):
    L[1][i] = 1
    
for i in range(2, N+1):
    for j in range(10):
        if j > 0:
            L[i][j] += L[i-1][j-1]
        if j < 9:
            L[i][j] += L[i-1][j+1]
        L[i][j] %= 1000000000

print(sum(L[N]) % 1000000000)
