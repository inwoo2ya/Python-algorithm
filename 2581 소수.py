m = int(input())
n = int(input())
s = []
for n in range(m,n+1):
    j = 0
    if n > 1 :
        for i in range(2,n):
            if n % i == 0 :
                j += 1
                break #2부터 n-1까지 나눈 몫이 0이면 j 증가후 for문을 끝냄
        if j == 0 :
            s.append(n) #j가 없으면 소수에 추가
        
if len(s) > 0 :
    print(sum(s))
    print(min(s))
else :
    print(-1)
