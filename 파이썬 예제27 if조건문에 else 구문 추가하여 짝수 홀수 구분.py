#입력을 받습니다.

number = input("정수 입력> ")
number = int(number)

#조건문 사용

if number % 2 ==0 :
    #조건이 참일때, 즉 짝수 조건
    print(number,"은 짝수 입니다.")

else :
    #조건이 거짓일때, 즉 홀수 조건
    print(number, "은 홀수 입니다.")
