x= int(input())

line = 1 # 라인에 들어있는 총 분수의 개수

while x>line :
    x -= line #ex14,13,11,8,4
    line+=1 #ex 1,2,3,4,5

if line%2 == 1 :
    a = line -x +1
    b = x

else :
    a = x
    b = line -x +1

print("{}/{}".format(a,b))
