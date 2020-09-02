N = int(input())

li = [0] * 1000001
li[1] = 1
li[2] = 2

for i in range(3, N+1):
    li[i] = (li[i-1] % 15746 + li[i-2] % 15746) % 15746

print(li[N])
