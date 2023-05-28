n = int(input())
stairs = [0 for i in range(301)]
d = [0 for i in range(301)]
max_sum = 0
for _ in range(n):
    stairs.append(int(input()))
d[0] = stairs[0] # 시작 점
d[1] = stairs[0] + stairs[1] #한계단 올라간 값
d[2] = max(stairs[1] + stairs[2],stairs[0]+stairs[2]) # 두번째 계단 밟고 한 계단 오를 때 와 첫번째 계단을 밟고 두 계단을 오를 때 비교
for i in range(3,n):
    d[i] = max(d[i-3]+stairs[i-1] + stairs[i],d[i-2]+stairs[i])
    # print("d[{}] =".format(i), d[i])
print(d[n-1])

