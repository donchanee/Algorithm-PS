N = int(input())

L = [0] * 31
L[2] = 3

for i in range(4, N+1, 2):
    L[i] = 2 + L[i-2] * 3 + sum(L[:i-2]) * 2

print(L[N])

# 3개 짜리여서 점화식을 찾는게 어렵
