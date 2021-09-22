n = int(input())
num = map(int,input().split())
s = 0 #소수
for nu in num :
    j = 0 #소수가 아닌걸 판별
    if nu > 1:
        for i in range(2,nu) :
            if nu % i == 0 :
                j += 1
        if j == 0 :
            s+=1
print(s)
