n = int(input())

for i in range(n) :
    a,b = input().split()
    a = int(a)
    for i in b :
        c= i*a
        print(c , end='')
    print()
            
