n = int(input())
for i in range(n):
    r = 0
    a = list(input().split())
    for j in range(len(a)):
        if a[j]== '@':
            r*=3
        elif a[j] == '%':
            r+=5
        elif a[j] == '#':
            r-=7
        else :
            r = float(a[j])
    print('%0.2f'%r)
