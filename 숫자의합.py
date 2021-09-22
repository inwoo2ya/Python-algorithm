i = int(input())
a = int(input())
sum = 0

for b in list(str(a)) :
    b=int(b)
    if i>0 :
        sum += b
        i -= 1
    else :
        pass
print(sum)
        
