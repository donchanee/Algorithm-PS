# https://www.acmicpc.net/problem/5585

N = 1000 - int(input())
li = [500, 100, 50, 10, 5, 1]
count = 0
for i in li:
    count += N // i
    N %= i
print(count)
