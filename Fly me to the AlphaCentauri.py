t = int(input())
result = []
for i in range(t) :
    x,y = map(int,input().split())
    d = y-x
    c = 0 #이동횟수
    m = 1 # 이동가능한거리
    sum = 0 #이동한거리의 합
    while True :
        if d > sum :
            sum += m
            c+=1
            if c % 2 == 0 :
                m+=1
        else :
            break
    result.append(c)

for n in result :
    print(n)
    
