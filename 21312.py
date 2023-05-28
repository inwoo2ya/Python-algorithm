import math
m = list(map(int,input().split()))
# 정진이는 맛이 홀수 > 짝수 or 똑같이 홀수나 짝수인경우 숫자가 더 큰 거
result = []

for i in m:
    if i % 2 :
        result.append(i)

if len(result) == 0 :
    print(math.prod(m))
else :
    print(math.prod(result))  