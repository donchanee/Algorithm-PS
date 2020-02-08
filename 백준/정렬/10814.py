# https://www.acmicpc.net/problem/10814 나이순 정렬

N=int(input())
a=[]
for i in range(N):
    b, c = map(str, input().split())
    b = int(b)
    a.append((b,c))
a.sort(key= lambda x: x[0])
for i in a:
    print(i[0], i[1])
