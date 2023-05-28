def check(x,y): # 뒤집기 함수
    for i in range(x,x+3):
        for j in range(y,y+3):
            if list_a[i][j] == 0:
                list_a[i][j] = 1
            else:
                list_a[i][j] = 0
            
n,m = map(int,input().split())
list_a = []
list_b = []
cnt = 0 #뒤집은 숫자 카운트

for _ in range(n):
    list_a.append(list(map(int,input())))
for _ in range(n):
    list_b.append(list(map(int,input())))

if (n <3 or m<3) and list_a != list_b:
    cnt = -1

else :
    for i in range(n-2):
        for j in range(m-2):
            if list_a[i][j] != list_b[i][j]:
                cnt +=1
                check(i,j)
if cnt != -1 :
    if list_a != list_b:
        cnt = -1
print(cnt)