def hanoi(n,a,b,c) : #a = 출발 b = 보조 c= 도착
    if n == 1 :
        print(a,c)
    else :
        hanoi(n-1, a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)


num = int(input())
sum = (2**num)-1
print(sum)
hanoi(num,1,2,3)
