# https://www.acmicpc.net/problem/11047 동전 0

N, K = map(int, input().split())
a=[]
cnt=0
for i in range(N):
    a.append(int(input()))
for i in reversed(a):
    if (K // i) > 0:
        cnt += K // i
        K = K % i
print(cnt)
