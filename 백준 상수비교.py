a,b = map(int,input().split())

a1 = (a%10)*100
a10 = (int(a/10)%10)*10
a100 = int(a/100)

b1 = (b%10)*100
b10 = (int(b/10)%10)*10
b100 = int(b/100)

A = a1+a10+a100
B = b1+b10+b100

if A >= B :
    print(A)
    
elif B>= A :
    print(B)
