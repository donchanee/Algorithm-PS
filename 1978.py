# https://www.acmicpc.net/problem/1978 소수 찾기

N = int(input())
a = list(map(int, input().split()))
counting = 0

for i in a:
    cnt = 0
    if(i == 1):
        continue
    for j in range(2, i + 1):
        if(i % j == 0):
            cnt += 1
    if(cnt == 1):
        counting += 1
print(counting)
