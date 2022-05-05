n,k = map(int,input().split())
bag = [[0,0]] 
bag_in = [[0 for _ in range(k+1)]for _ in range(n+1)]
for _ in range(n):
    bag.append(list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        weight = bag[i][0]
        value = bag[i][1]
        
        if j< weight:
            bag_in[i][j] = bag_in[i-1][j] # weight보다 작으면 위의 값을 그대로 가져옴
        else :
            bag_in[i][j] = max(value + bag_in[i-1][j-weight] ,bag_in[i-1][j])

print(bag_in[n][k])
