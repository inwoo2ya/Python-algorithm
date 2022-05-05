import sys
from collections import deque
n = int(input())
ball_list=[]
ball_batch=deque([i for i in range(1,n+1)])
ball = deque(list(map(int,sys.stdin.readline().split())))

while ball :
    p = ball[0]#맨첫번째거 우선 빼
    if p > 0:
        ball.popleft()
        ball.rotate(-p+1)
        ball_list.append(ball_batch.popleft())
        ball_batch.rotate(-p+1)
    else:
        
        ball.popleft()
        ball.rotate(-p)
        ball_list.append(ball_batch.popleft())
        ball_batch.rotate(-p)

for i in ball_list:
    print(i,end=" ")
