n = int(input()) # 약수의 개수
m = list(map(int,input().split()))

m.sort()
result = m[0] * m[-1]

print(result)
