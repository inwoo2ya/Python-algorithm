a,b,c,d,e,f = map(int,input().split())

for x in range(-999,1000): # -999<= x <= 999
    for y in range(-999,1000): # -999<= y <= 999
        if (a*x) + (b*y) == c and (d*x) + (e*y) == f:
            print(x,y)