n = int(input())
data =[]
rank =[]

for i in range(n) : 
    m,h = map(int,input().split())
    data.append((m,h))#몸무게와 키 리스트에 삽입 
    
for i in range(n) :
    count = 0
    for j in range(n) :
        if data[i][0] < data[j][0] and data[i][1] < data[j][1] : #몸무게와 키가 자신보다 큰 사람인지 아닌지 비교
            count += 1 #큰 사람이 있으면 숫자를 올린다.
        else :
            continue #없으면 계속 진행
    rank.append(count+1) #순위는 1부터 시작

for i in rank :
    print(i,end=" ") #출
