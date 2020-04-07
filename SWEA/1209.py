# import sys

for _ in range(10):
    case = int(input())
    max = 0
    a = []
    for _ in range(100):
        a.append(list(map(int, input().split())))
        # a.append(list(map(int, sys.stdin.readline().split())))
        # Swea에선 sys 라이브러리를 사용하지 못하게 한다... 외부라이브러리라 그런가..?

    for i in a:
        if sum(i) > max:
            max = sum(i)

    for i in range(100):
        sum1 = 0
        for j in range(100):
            sum1 += a[j][i]
        if sum1 > max:
            max = sum1

    sum1 = 0
    for i in range(100):
        sum1 += a[i][i]
    if sum1 > max:
        max = sum1

    sum1 = 0
    for i in range(100):
        sum1 += a[99-i][i]
    if sum1 > max:
        max = sum1

    print("#",case," ",max,sep="")
