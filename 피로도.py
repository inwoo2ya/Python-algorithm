a,b,c,m = map(int,input().split())
p = 0 #피로도
hour = 24 #하루
w = 0 #일한양

for i in range(hour):
    if a>m :
        break
    if p <= m :
        if p>m-a :
            p -=c
        else :
            w += b
            p += a
    else :
        break
print(w)
    
