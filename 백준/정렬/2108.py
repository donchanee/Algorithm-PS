import sys
from collections import Counter

N = int(sys.stdin.readline())
a=[]
for _ in range(N):
    a.append(int(sys.stdin.readline()))

def mode(x):
    mode_dict = Counter(x)
    modes = mode_dict.most_common()
    if len(x) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]
    
    return mod

avg = round(sum(a)/len(a))
b = sorted(a)
mid = b[len(b)//2]
max_in = mode(b)
ran = max(a)-min(a)
print(avg,mid,max_in,ran,sep='\n')

# 최빈값 Counter import가 문제였다.
