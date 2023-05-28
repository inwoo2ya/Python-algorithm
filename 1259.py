while True:
    n = input()
    if n == '0' :
        break
    else:
        if n ==  n[::-1]: # 거꾸로 뒤로 숫자 세기
            print('yes')
        else :
            print('no')