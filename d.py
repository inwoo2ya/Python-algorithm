def fact(n) :
    f = 1
    for i in range(1,n+1) :
        f *= i
    print(f)
            
num = int(input())
fact(num)
