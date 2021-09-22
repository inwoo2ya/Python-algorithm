#그룹단어를 센다
n = int(input())
result = 0
for i in range(n) :
    str = input()
    for j in range(len(str)) :
        if j !=len(str)-1 :
            if str[j] == str[j+1] :
                pass
            elif str[j] in str[j+1 :] :
                break #for문을 벗어남
        else :
            result += 1
            
print(result)
