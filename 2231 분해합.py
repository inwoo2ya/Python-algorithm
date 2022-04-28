n = int(input())

for i in range(n+1):
    m = sum(map(int,str(i))) # if 231일경우 m= 2+3+1
    msum = m+i #if 231일 경우 msum = 2+3+1  +  231

    if n == msum :
        print(i)
        break
    elif n == i :
        print(0)
        break
