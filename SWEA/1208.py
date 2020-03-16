for j in range(10):
    T = int(input())
    a = list(map(int, input().split()))
    for i in range(T):
        a[a.index(max(a))] -= 1
        a[a.index(min(a))] += 1
            
    print("#",j+1," ",max(a)-min(a),sep="")

// 최댓값 - 최솟값만을 T번 반복해주었다.
