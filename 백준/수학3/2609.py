# https://www.acmicpc.net/problem/2609 최대공약수와 최소공배수

from math import gcd

a,b = map(int, input().split())
print(gcd(a,b))
print(a*b//gcd(a,b))
