N, M, L = map(int, input().split())

li = [0] * N
flag = 0
result = 0
while M not in li:
    li[flag] += 1
    if li[flag] % 2 == 1:
        flag = (flag+L) % N
    else:
        flag = (flag-L) % N
    result+= 1

print(result-1)
