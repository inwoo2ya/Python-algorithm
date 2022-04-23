n = int(input())
r=[]
for i in range(n):
    a,b,c = map(int,input().split())
    if a == b == c:
        result= 10000+a*1000
        r.append(result)
    elif a==b:
        result = 1000+a*100
        r.append(result)
    elif b==c:
        result = 1000+b*100
        r.append(result)
    elif c==a:
        result = 1000+c*100
        r.append(result)
    else:
        result = 100*max(a,b,c)
        r.append(result)

print(max(r))
        
