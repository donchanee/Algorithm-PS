#https://www.acmicpc.net/problem/11650 좌표 정렬하기

N=int(input())
a=[]
for i in range(N):
    a.append(list(map(int,input().split())))
a.sort()
for i in a:
    print(i[0],i[1])
