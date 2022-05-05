import heapq

v,e = map(int,input().split()) #v = 정점의 개수 , e = 간선의 개수
k = int(input()) #시작 점
route = [[]for _ in range(v+1)]
INF = int(1e9)
dp = [INF]*(v+1) #가중치

heap=[]
def d(k):
    dp[k] = 0
    heapq.heappush(heap,(0,k)) #heap에 0과 k를 넣어줌

#힙에 원소에 없을때까지 반복
    while heap:
        wei, now = heapq.heappop(heap)
        print(wei , now)

        if dp[now] < wei:
            continue

for i in range(e):
    u,v,w = map(int,input().split())
    route[u].append((v,w))

d(k)

for i in range(1,v+1):
    if dp[i] == INF:
        print("INF")
    else :
        print(dp[i])
print(route)
