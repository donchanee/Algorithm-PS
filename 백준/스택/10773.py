# https://www.acmicpc.net/problem/10773 제로

K=int(input())
a=[]
for i in range(K):
    b=int(input())
    if b != 0:
        a.append(b)
    else:
        a.pop()
print(sum(a))
