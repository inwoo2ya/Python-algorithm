n = int(input())
array=[]
for i in range(n):
    xy = list(map(int,input().split()))
    array.append(xy)
array.sort()
for j in array :
    print(j[0],j[1])
    
