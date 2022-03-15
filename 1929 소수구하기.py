def isprime(num) : #에라토스테네스의 체 소수 판별 알고리즘 함수
    if num == 1 :
        return False
    else :
        for i in range(2, int(num**0.5)+1):
            if num % i == 0 :
                return False
        return True
    
m, n = map(int,input().split())

for num in range(m,n+1):
    if isprime(num):
        print(num)
# 인자로 들어온 수의 제곱근 까지만 확인하여 소수인지 아닌지를 검증하는 함수를 사용
