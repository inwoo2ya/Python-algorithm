import sys
from collections import deque
n = int(input())

deq = deque()
for _ in range(n):
    q = sys.stdin.readline().split()
    i = 0
    if len(q) == 2:
        i = q[1]
    q = q[0]

    if q =='push_front':
        deq.appendleft(i)
    elif q=='push_back':
        deq.append(i)
    elif q=='pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif q == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif q == 'size':
        print(len(deq))
    elif q == 'empty':
        if len(deq) == 0:
            print(1)
        else :
            print(0)
    elif q == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif q == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
                  
