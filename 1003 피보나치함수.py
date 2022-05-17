z = [1,0,1]#0의 호출 횟수
o = [0,1,1]#1의 호출 횟수

# 1과 0의 호출의횟수는 n = 2까지 같다 이것을 이용하여 푼 문제
def fibonacci(n):
    if n >= len(z):
        for i in range(len(z),n+1):
            z.append(z[i-1] + z[i-2]) 
            o.append(o[i-1] + o[i-2])
    print(z[n] , o[n])
    
    
t = int(input())
for _ in range(t):
    fibonacci(int(input()))
