max_value = 0
a = 0
b = 0

for i in range(1,100) :
    j = 100 - i

    # 최댓값 구하기
    current = i * j
    if max_value < current : # if max_value < i*j
        a = i
        b = j
        max_value = current
        #max_value = i*j 
print("최대가 되는 경우 : {} * {} = {} ".format(a,b,max_value))
