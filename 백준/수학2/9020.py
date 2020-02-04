# https://www.acmicpc.net/problem/9020 골드바흐의 추측

'''
시간초과
n=10000*2
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

N = int(input())

for i in range(0,N):
    M = int(input())
    flag = 10000
    res1 = 0
    res2 = 0
    for i in primes:
        for j in primes:  # 이중포문 시간초과 예상 할때마다 구하니까 미리 구해둔 체가 필요없었다
            if i > M or j > M:
                break
            if i+j == M and flag > abs(i-j):
                res1 = i
                res2 = j
                flag = abs(i-j)

    print(res1,res2)
'''

n=10000*2
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

N = int(input())

for i in range(0,N):
    M = int(input())
    
    b = M // 2  # 절반으로 나누고 절반 이상부터 찾아나가는데

    for j in range(b, M+1):
        if a[j]:   # 에스토스테네스의 체 안에 소수로 표시되어 있으면
            if a[M-j]:   # 주어진 수에서 그 수를 빼서
                print(M-j, j)   # 결과값을 찾는다.
                break


