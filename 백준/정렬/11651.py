#https://www.acmicpc.net/problem/11651 좌표 정렬하기 2

N=int(input())
a=[]
for i in range(N):
    a.append(list(map(int,input().split())))
a.sort(key=lambda x: (x[1],x))  # lambda 를 활용, x[1]을 먼저 정렬함
for i in a:
    print(i[0],i[1])
