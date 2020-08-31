N = int(input())

L = [0] * 1001
L[1] = 1
L[2] = 2

for i in range(3,N+1):
    L[i] = (L[i-1] + L[i-2]) % 10007

print(L[N])
