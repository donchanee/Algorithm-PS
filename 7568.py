# https://www.acmicpc.net/problem/7568 덩치 / enumerate 의 필요성!

N = int(input())
a=[]
b=[1] * N
for i in range(N):
    a.append(list(map(int, input().split())))

for v, i in enumerate(a):
    for j in a:
        if i[0] < j[0] and i[1] < j[1]:
            b[v]+=1
            
print(' '.join(map(str, b)))
