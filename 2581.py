# https://www.acmicpc.net/problem/2581 소수

M = int(input())
N = int(input())
a = list(range(M, N+1))
summ = 0
minn = 10001

for i in a:
    cnt = 0
    if(i == 1):
        continue
    for j in range(2, i + 1):
        if(i % j == 0):
            cnt += 1
    if(cnt == 1):
        summ += i
        if minn > i:
            minn = i
        
if minn == 10001:
    print(-1)
else:
    print(summ)
    print(minn)
