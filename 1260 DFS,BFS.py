from collections import deque
def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in graph[n] :
        if not visited[i]:
            dfs(i)
    

    
def bfs(n):
    q = deque([n]) #deque화 초기화 함수
    visited[n] = True
    while q:
        v = q.popleft() # 덱의 가장 왼쪽에 있는 원소를 덱에서 제거하고, 그값을 리
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i) #덱의 오른쪽에 삽입
                visited[i] = True




n,m,v = map(int,input().split())
graph = [[]for i in range(n+1)]

for i in range(m):
    r,node = map(int,input().split())
    graph[r].append(node)
    graph[node].append(r)
for i in range(1,n+1):
    graph[i].sort()

visited = [False] * (n+1) #방문을 했는지 확인하고자하여 변수 선언
dfs(v)
visited = [False] * (n+1)
print()
bfs(v)

