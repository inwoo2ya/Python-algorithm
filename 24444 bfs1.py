from collections import deque
import sys
n,m,r = map(int,sys.stdin.readline().split())
visited = [0]*(n+1)
e = [[]for i in range(n+1)]
result = []
def bfs(r):
    q = deque([r])
    visited[r] = 1 #첫번째 방문 정점
    cnt = 2 # 2번째 방문 정
    while q:
        v = q.popleft()
        for i in e[v]:
            if not visited[i]:
                visited[i] = cnt
                q.append(i)
                cnt+=1
    
        
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    e[u].append(v)
    e[v].append(u)

for i in range(1,n+1):
    e[i].sort()
    
bfs(r)
for j in range(1,n+1):
    print(visited[j])
