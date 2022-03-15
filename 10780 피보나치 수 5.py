def fibo(n) :
    fibo = []

    for i in range(n+1) :
        if i == 0 :
            fibo.append(0)
        elif i == 1 :
            fibo.append(1)
        else :
            f = fibo[i-1] + fibo[i-2]
            fibo.insert(i,f)

    print(fibo[n])

num = int(input())

fibo(num)
