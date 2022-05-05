n = int(input())

p = list(map(int,input().split()))
result=0
p.sort()
for i in range(n):
    if i==0:
        continue
    else :
        p[i] = p[i]+p[i-1]

print(sum(p))
