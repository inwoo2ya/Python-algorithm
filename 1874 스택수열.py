n = int(input())
pstack=[]
s= []
tmp = True
cnt = 1 # 들어가는 숫자
for i in range(n):
    a = int(input())
    while cnt <= a: # 입력한 숫자(pop)가 들어가는 숫자(cnt)보다 클 때
        s.append(cnt) # push
        pstack.append('+')
        cnt+=1 #다음 push할 숫자 +1
    if s[-1] == a: #만약 숫자가 스택에 있는 숫자와 같을때 
        s.pop()#pop
        pstack.append('-')
    else:
        tmp = False # a가 cnt보다 작고 , 스택 맨위에 있지도 않을 때
if tmp == False:
    print('NO')
else:
    for i in pstack:
        print(i)
