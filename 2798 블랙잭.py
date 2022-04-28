n,m = map(int,input().split())
card = list(map(int,input().split()))
result = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if card[i] + card[j] + card[k] >m :
                continue
            else:
                result = max(result,card[i]+card[j]+card[k]) # result와 card값들을 더한 것중에 더 큰 것을 비교후 result값에 대입

print(result)
        
