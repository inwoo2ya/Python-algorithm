n = int(input())
3 <= n <= 5000
fg = 0
while n>=0 :
    if n%5 == 0 : #5의배수일때의 조건문
        fg = fg + (n//5) # 5로 나눈몫을 더해줌
        print(fg)
        break
    n -= 3 #5의 배수가 될때 까지 3을 빼줌 ㅆㅂ
    fg +=1 #3kg짜리 봉지를 하나 더함
else :
    print(-1)
