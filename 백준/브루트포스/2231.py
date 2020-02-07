#https://www.acmicpc.net/problem/2231 분해합

N = int(input())

a = []
e = N
while e > 0:
    a.append(e%10)
    e = e // 10

b = N - len(a) * 9
min = 1000000

for i in range(b, N+1):
    c = []
    d = i
    while i > 0:
        c.append(i%10)
        i = i // 10
    if sum(c) + d == N and d < min:
        min = d
        
if min == 1000000:
    min = 0
    
print(min)
