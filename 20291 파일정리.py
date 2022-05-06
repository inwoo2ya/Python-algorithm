n = int(input())
dic = {}

for i in range(n):
    file = input().split(".")[1] #[0]은 파일 이름 [1]은 파일 확장자
    if file not in dic :
        dic[file] = 1
    else :
        dic[file] +=1

file = list(dic.keys()) #dic에서 키들을 꺼내서 리스트로 제작
file.sort()

for i in file:
    print(i, dic[i])
