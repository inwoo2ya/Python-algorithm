import sys
def f(n):
    num = 1
    for i in range(1,n+1):
        num *=i
    return num
t = int(sys.stdin.readline())

for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
# 조합 공식 
    if n > m : #nCm
        result = f(n)//(f(m) * f(n-m))
        print(result)
    else : #mCn
        result = f(m)//(f(n) * f(m-n))
        print(result)