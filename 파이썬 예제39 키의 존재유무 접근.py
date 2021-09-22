#딕셔너리 선언
dictionary = {
    "name" : "쉔",
    "type" : ["닌자","조율자"],
    "skin" : ["지옥의 쉔","기본"],
    "origin" : "japan?"
    }

#사용자로부터 입력을 받습니다.
key = input("> 접근하고자 하는 키: ")

#출력

if key in dictionary:
    print(dictionary[key])
else :
    print("존재하지 않는 키에 접근하고 있습니다.")
