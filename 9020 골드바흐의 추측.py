# 다시 해보자!
def isprime(num) : #에라토스테네스의 체 소수 판별 알고리즘 함수
    if num == 1 :
        return False
    else :
        for i in range(2, int(num**0.5)+1):
            if num % i == 0 :
                return False
        return True     #소수 구하는 방식은 위와 같다.
    
T = int(input())

for i in range(0,T):
    n = int(input())
    m = n//2 #n을 반으로 나눈다
    all_list = list(range(2,n)) 
    s_list =[]
    for i in all_list :
        if isprime(i):
            s_list.append(i)
    for j in range(m,1,-1): #차이가 적은 두 수를 구하기 위해서 큰수부터
        if (n - j in s_list) and (j in s_list) :
            print(j, n-j)
            break
        
