# 딕셔너리를 선언
dictionary = {
    "name" : "쉔",
    "type" : ["닌자","조율자"],
    "skin" : ["지옥의 쉔","기본"],
    "origin" : "japan?"
    }
#존재하지 않는 키에 접근
value = dictionary.get("존재하지 않는 키")
print("값: ",value)

#None 확인 방법
if value == None:
    print("존재하지 않는 키에 접근했었습니다.")
