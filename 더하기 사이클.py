a = int(input())
A = a
n = 0 
t = 0

while 1 :
    b= a//10
    c = a%10
    t = b + c
    na = (c)*10 + t%10
    n += 1
    a = na
    if A == a :
        break
    
print(n)
