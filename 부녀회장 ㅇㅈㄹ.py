T = int(input())

for i in range(T) :
    k = int(input())
    n = int(input())
    r = [x for x in range(1,n+1)] # 1,2,3,4...# 이거 몰랐었음
    print(r)
    for a in range(k) :
        for i in range(1,n) :
             r[i] += r[i-1]
             
    print(r[-1])
