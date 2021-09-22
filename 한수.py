def Hnumber(n):
    s = 0
    for i in range(1,n+1) :
        if 0 < i <100:
            s += 1
        if 100 <= i <= 1000 :
            a = i//100
            b = (i-100*a)//10
            c = i%10
            if ( a-b == b-c) :
                s +=1
            else :
                pass
            
    return s

n = int(input())
print(Hnumber(n))
