n = int(input())
r1 = 100#창영
r2 = 100#상덕
for i in range(n):
    a, b = map(int,input().split())
    if a>b :
        r2 -= a
    elif a<b :
        r1 -= b
    else :
        continue

print(r1)
print(r2)
