def d(n):
    a = 0
    for i in list(str(n)) :
        a = a +int(i) # 1) 0 + 7    2) 7 + 5   3) 12 + 0
    return int(n) + a #750 + 12
a = list()
for i in range(1,10001) :
    a.append(d(i))
    #-------------self넘버 만드는과정---------
for i in range(1,10001) :
    if i in a:
        pass
    else :
        print(i)
