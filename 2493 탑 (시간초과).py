import sys
n = int(sys.stdin.readline())
tower = list(map(int,sys.stdin.readline().split()))
result = [0]*n

for i in range(n):
    if i == 0:
       continue #첫번째 타워는 왼쪽에 수신할 타워가 없음
    else:
        for j in range(1,i+1):
            if tower[i] <= tower[i-j]:
                result[i] = (i-j+1)
                break
            
            
for t in result:
    print(t, end=" ")
