c = int(input())

for i in range(c) :
    n = list(map(int,input().split()))
    exc = 0
    avg= sum(n[1:])/n[0]
    
    for i in n[1:] :
        if i > avg :
            exc += 1
            
    per = exc/n[0]*100
    print(f'{per:.3f}%')
