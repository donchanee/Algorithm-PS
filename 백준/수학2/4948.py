# https://www.acmicpc.net/problem/4948 베르트랑 공준

n=123456*2
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

while True:
    N = int(input())
    cnt = 0
    if N == 0:
        break
    for i in range(N+1, 2*N+1):
        if a[i] == True:
            cnt += 1
    print(cnt)
