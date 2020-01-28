# https://www.acmicpc.net/problem/10870 피보나치 수

def fibo (num):
    if num<2:
        return num
    else:
        return fibo(num-1)+fibo(num-2)

n = int(input())

print(fibo(n))
