#입력을 받습니다.

number = input("정수 입력> ")
last_character = number[-1]

#짝수
if last_character in "02468":
    print("짝수 입니다.")

#홀수
if last_character in "13579":
    print("홀수 입니다.")
