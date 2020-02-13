# https://www.acmicpc.net/problem/2748 피보나치 수 2

T = int(input())
a = [True, True] + [False] * T
b = [0,1]

def fibo(n):
    if n<2:
        return n
    if a[n] == True:
        return b[n]
    return fibo(n-1) + fibo(n-2)

for i in range(T-1):
    b.append(fibo(i+2))
    a[i+2] = True

print(b[T])
