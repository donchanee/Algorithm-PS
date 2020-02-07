# https://www.acmicpc.net/problem/10872 팩토리얼

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n = int(input())
print(factorial(n))
