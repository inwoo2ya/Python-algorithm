n ,m = map(int,input().split())
l = list(map(int,input().split()))

for _ in range(m):
    a,b,c = map(int,input().split())

    if a == 1 :
        l[b-1] = c

    elif a == 2 :
        for i in range(b-1,c):
            if l[i] == 0:
                l[i] = 1
            else :
                l[i] = 0

    elif a == 3 :
        for i in range(b-1,c):
            l[i] = 0

    elif a == 4 :
        for i in range(b-1,c):
            l[i] = 1

for j in l :
    print(j ,end=" ")
        
