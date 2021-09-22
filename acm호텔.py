t = int(input())
result = []
floor = 0
for i in range(t):
    h,w,n = map(int,input().split())
    for i in range(1,w+1) :
        floor += i 
        for j in range(1,h+1) :
            n-=1
            floor = 100*j + i
            if n == 0 :
                break
            else :
                if j == h:
                    break
        if n == 0 :
                break
    result.append(floor)

for room in result :
    print(room)
