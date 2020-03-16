from collections import Counter
T = int(input())

for i in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    print("#",N,' ',Counter(a).most_common(n=1)[0][0], sep='')

// Collections 가 생각보다 많이 쓰임.
