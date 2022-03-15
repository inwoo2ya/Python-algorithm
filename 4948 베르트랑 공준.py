# 어려워요...;;;
def isprime(num) : #에라토스테네스의 체 소수 판별 알고리즘 함수
    if num == 1 :
        return False
    else :
        for i in range(2, int(num**0.5)+1):
            if num % i == 0 :
                return False
        return True     #소수 구하는 방식은 위와 같다.

all_list = list(range(2,246912))    #문제에서 제한한 범위
memo = []   #for문 밖에 리스트 정의

for i in all_list: #2부터 2*123,456 범
    if isprime(i) : # 함수에 해당
        memo.append(i) #리스트에 추가

n = int(input())

while 1 :
    m = 2*n
    count = 0
    if n == 0 :
        break
    else :
        for a in memo : #memo리스트 중에서
            if n < a <= m: #입력한 값의 범위 내에서 값이 있으
                count +=1 #있을 때 마다 카운트 +1
        print(count)
    n = int(input())    #0 입력받기 전까지 계속 해야하므 입력 받음
