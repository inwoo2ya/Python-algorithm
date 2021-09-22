n = int(input())
for i in range(n) :
    a = list(input())
    score = 0
    r = 1
    for i in range(len(a)) :
        if a[i] == "O" :
            score += r
            r +=1

        else :
           r= 1
    print(score)
