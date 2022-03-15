m = int(input())
for i in range(1,m+1) :
    num = sum(map(int,str(i))) # 계속 반복해서 m까지 올라가면서 각 자릿수 int로 바꿔서 더하기
    print(num,"+",i)
    nsum = i + num
    if m == nsum :
        print(i)
        break
    if m == i :
        print(0)
        break
    
