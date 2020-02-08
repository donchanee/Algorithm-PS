#https://www.acmicpc.net/problem/1181 단어 정렬

N=int(input())
a=[]
for i in range(N):
    a.append(input())
a=list(set(a))
a.sort(key=lambda x: (len(x),x))
for i in a:
    print(i)
