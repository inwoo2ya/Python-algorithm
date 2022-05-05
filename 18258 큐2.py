import sys
from collections import deque
n = int(input())

queue = deque()
for _ in range(n):
    q = sys.stdin.readline().split()
    i = 0
    if len(q) == 2:
        i = q[1]
    q = q[0]

    if q =='push':
        queue.append(i)
    elif q == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif q == 'size':
        print(len(queue))
    elif q == 'empty':
        if len(queue) == 0:
            print(1)
        else :
            print(0)
    elif q == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif q == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
                  
