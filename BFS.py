#BFS

from collections import deque

def bfs(graph, n, v):
    queue = deque([n])
    #현재 노드 방문 처리
    print(queue)
    v[n] = True

    # 큐가 완전히 빌 때까지
    while queue :
        # 큐에 삽입된 순서대로 노드 하나 꺼내기
        q = queue.popleft()
        #탐색 순서 출력
        print(q, end = '')
        #현재 처리 중인 노드에서 방문하지 않은 인접 노드를 모두 큐에 삽입
        for i in graph[q]:
            if not (v[i]):
                queue.append(i)
                v[i] = True
    
visited = [False] * 9
graph = [
    [],
    [2, 3],
    [1, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7, 8],
    [6, 8],
    [2, 6, 7]
]
bfs(graph,1,visited)
