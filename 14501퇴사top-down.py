import sys
n = int(sys.stdin.readline())
s = []

for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    s.append(a)
dp = [0 for _ in range(n+1)]
#topdown
for i in range(n-1,-1,-1):
    # i일에 상담을 하는 것이 퇴사일을 넘기며 상담을 하지 않음
    if i + s[i][0] > n:
        dp[i] = dp[i+1]
    else:
        # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택
        dp[i] = max(dp[i+1],s[i][1]+ dp[i+s[i][0]])
        
print(dp[0])