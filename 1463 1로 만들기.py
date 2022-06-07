n = int(input())
cnt = [0] * (n+1)
# 각 숫자마다 카운트 
for i in range(2,n+1): # n값을 1로 바꾸는 횟수를 다 계산

    cnt[i] = cnt[i-1] +1 # i=2일때, 먼저 1을  시작 i=1은 이미 1이기때문에 넣을 필요 x 즉,0
    #i = 6 이면 if 둘다 지나침 
    if i%2 == 0:
        cnt[i] = min(cnt[i],cnt[i//2]+1) # i=6  cnt[6] = 3 ,cnt[3] = 2 +1(오른쪽 거 선택) 값이 같기 때문에 cnt[6] = 3
    if i%3 == 0:
        cnt[i] = min(cnt[i],cnt[i//3]+1) # i=6 cnt[6] = 3 , cnt[2] = 1 +1(오른쪽 선택) cnt[6] = 2로 변경

print(cnt[n])
