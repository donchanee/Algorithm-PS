# https://www.acmicpc.net/problem/9095

def inte(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return inte(n-1) + inte(n-2) + inte(n-3)

T = int(input())

for i in range(T):
    n = int(input())
    result = inte(n)
    print(result)
