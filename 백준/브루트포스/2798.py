# https://www.acmicpc.net/problem/2798 블랙잭

N, M = map(int, input().split())
a = list(map(int, input().split()))

max = 0

for i in a:
    for j in a:
        for k in a:
            if i+j+k <= M and i+j+k > max and i != j and j != k and i != k:
                max = i+j+k

print(max)
