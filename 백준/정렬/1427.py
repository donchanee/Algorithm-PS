#https://www.acmicpc.net/problem/1427 소트인사이드

N=input()
a=[]
for i in range(len(N)):
    a.append(int(N[i]))
a.sort(reverse=True)
for i in range(len(a)):
    print(a[i], end='')
