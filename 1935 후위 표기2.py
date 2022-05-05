n = int(input())
s = input()
num = [0]*n
for i in range(n):
    num[i] = int(input())

s_list = []
for i in s:
    if i =='*'or i=='+' or i == '/' or i =='-': # 연산자가 나온다면 피연산자(숫자) 두 개를 꺼내준다 스택에서 
        b = s_list.pop()
        a = s_list.pop()
        if i == '*' :
            s_list.append(a*b)
        elif i == '+':
            s_list.append(a+b)
        elif i== '-':
            s_list.append(a-b)
        elif i=='/' :
            s_list.append(a/b)
    else:
        if 'A' <= i <= 'Z' :
            s_list.append(num[ord(i)-ord('A')]) #ord함수는 str을 숫자로 변환 그래서 숫자값으로 s_list에 저장
print("%.2f" %s_list[0])
