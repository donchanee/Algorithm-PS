# https://www.acmicpc.net/problem/2751 수 정렬하기 2

N = int(input())
a=[]
for i in range(N):
    a.append(int(input()))
a.sort()
for i in a:
    print(i)
