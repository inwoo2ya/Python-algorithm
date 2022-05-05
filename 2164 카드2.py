from collections import deque
n = int(input())
deq = deque()
for i in range(1,n+1):
    deq.append(i)

while len(deq):
    a = deq.popleft() # 맨 위
    if not deq :
        print(a)
        break
    b = deq.popleft() # 맨 위-> 맨 밑
    deq.append(b)
