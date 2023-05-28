import sys
n = int(sys.stdin.readline())

s = []
for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    s.append(a)

# bottom -up 버전 dp
dp = [0 for i in range(n+1)]
# t = 상담을 완료하는 걸리는 시간 (일 수)
    # p = 상담을 했을 때 받을 수 있는 금액
for i in range(n): # i 가 일하는 날
    for j in range(i+s[i][0],n+1): #j는 상담이 가능한 모든 날짜 즉, i+상담기간
        
        if dp[j] < dp[i] + s[i][1]:
            dp[j] = dp[i] + s[i][1]
print(dp[-1])
