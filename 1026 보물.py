n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
r=0

for i in range(n):
    r += max(a) * min(b)
    a.remove(max(a))
    b.remove(min(b))
print(r)
