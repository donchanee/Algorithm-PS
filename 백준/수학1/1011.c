#https://www.acmicpc.net/problem/1011

def calculate(d):
    maximum=0
    i=1
    while(maximum <d):
        maximum = maximum +(i+1)//2
        i=i+1
    return i-1

n=int(input())
for i in range(n):
    str = input().split()
    d=int(str[1]) - int(str[0])
    print(calculate(d))
