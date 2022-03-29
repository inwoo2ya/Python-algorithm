n = int(input())
array = []
for i in range(n):
    yx = list(map(int,input().split()))
    array.append(yx)
array.sort(key=lambda x:(x[1],x[0])) #정렬기준 정해주는 함수, x[1]로 부터봐서 정렬 

for i in array:
    print(i[0],i[1])
