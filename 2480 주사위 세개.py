a,b,c = map(int,input().split())
box =[]
box.append(a)
box.append(b)
box.append(c)
if box.count(a) == 3 :
    result = 10000 + (a*1000)
elif box.count(a) == 2 or box.count(b) == 2 or box.count(c) == 2 :
    if box.count(a) == 2 :
        result = 1000 + (a*100)
    else :
        result = 1000 + (b*100)
else :
    result = 100*max(box)

print(result)
