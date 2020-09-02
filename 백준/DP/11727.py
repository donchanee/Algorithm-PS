N = int(input())

L = [0] * 1001
L[1] = 1
L[2] = 3

for i in range(3,N+1):
    L[i] = (L[i-1] + 2 * L[i-2]) % 10007

print(L[N])


# dp는 무조건 점화식을 세우고, 유사도를 찾는다
# dp인지 구분은 어떻게?
