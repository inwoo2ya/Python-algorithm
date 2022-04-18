n = input().split('-')
s=[]
for i in n:
    l = 0
    m = i.split('+')
    for j in m:
        l += int(j)
    s.append(l)
    
r = s[0] # - 전의 값
for i in range(1,len(s)):
    r -= s[i] # 나머지 -값을 더해준다.
print(r)
