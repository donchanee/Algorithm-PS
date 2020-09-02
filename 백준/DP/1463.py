# https://www.acmicpc.net/problem/1463 1로 만들기

N = int(input())
count = 0
R=[N]
def cal(P):
    li = []
    for i in P:
        li.append(i-1)
        if i%3 == 0:
            li.append(i//3)
        if i%2 == 0:
            li.append(i//2)
    return li
 
while N!=1:
    temp = R[:]
    R = []
    R = cal(temp)
    count +=1
    if min(R) == 1:
        break

print(count)
