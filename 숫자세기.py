a = int(input())
b = int(input())
c = int(input())

sum = a*b*c
result = list(map(int,str(sum)))
for i in range(10) :
    count = result.count(i)
    print(count)
