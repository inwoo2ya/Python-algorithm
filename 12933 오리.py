duck = input()
quack = ['q','u','a','c','k']
visited = [False]*len(duck)
cnt = 0

if len(duck) % 5 != 0 : # 문자열의 길이가 5의배수가 아님
    print(-1)
    exit()

for i in range(len(duck)) :
    if duck[i] == 'q' and not visited[i]: #방문하지 않았고, q인 곳은 시작구간
        start = True
        k = 0
        for j in range(i,len(duck)):
            if not visited[j] and duck[j] == quack[k]:
                visited[j] = True
                if duck[j] == 'k' :
                    if start :
                        cnt +=1
                        start = False
                    k = 0
                    continue
                k+=1
if not all(visited) or cnt == 0:
    print(-1)
else :
    print(cnt)
    
