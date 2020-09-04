N, K = map(int, input().split())

L = list(range(1,N+1))
M = 0

print('<', end='')
while len(L):
    M = (M + (K-1)) % len(L)
    if len(L)==1:
        print(L.pop(M), sep='', end='')
    else:
        print(L.pop(M), ', ', sep='', end='')
print('>')

# 이거보다 Pop한걸 list에 넣어서 출력하는 경우가 4ms 더 빠르다. 왜지?
