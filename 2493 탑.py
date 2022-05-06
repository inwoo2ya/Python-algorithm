import sys
n = int(sys.stdin.readline())
tower = list(map(int,sys.stdin.readline().split()))
result = [0]*n
stack = []

for i in range(len(tower)-1,-1,-1):
    if len(stack)==0:
       stack.append([i, tower[i]]) #ex) stack [0,6]
       #첫번째 타워는 왼쪽에 수신할 타워가 없음
    else:
        while tower[i] > stack[len(stack)-1][1]:
           # ex) i=1 일 경우 tower[i] : 9 > stack[0][1] : 6
           t = stack.pop() # 위치를 빼감 [0] 아마도?
           print(t)
           result[t[0]] = i+1
           print(result)

           if len(stack) == 0:
               break

        stack.append([i,tower[i]])
        
            
for t in result:
    print(t, end=" ")
