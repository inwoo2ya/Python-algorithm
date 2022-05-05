import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
y = []
q = deque()
for i in range(1,n+1):
    q.append(i)
while len(q):
    q.rotate(-k) # rotate => 목록을 회전시킴 -1 : 시계반대방향 1:시계방
    y.append(q.pop())
print('<' + ', ' .join(map(str,y)) + '>')
