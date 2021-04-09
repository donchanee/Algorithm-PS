N = int(input())
li = list(map(int, input().split()))
s = sorted(list(set(li)))

s = {s[i]:i for i in range(len(s))}
print(*[s[i] for i in li])

# Unpacking 이 ''.join 말고도 *로도 가능함..
