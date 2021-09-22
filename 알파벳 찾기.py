a = str(input())
b = list(range(26))
for i in range(len(b)) :
    asci = chr(i+97)
    if asci in a :
        b[i] = a.index(asci)
    else :
        b[i]= -1
    print(b[i], end=" ")
