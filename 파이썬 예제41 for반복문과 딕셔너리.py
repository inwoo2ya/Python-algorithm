# 딕셔너리 선언
dictionary = {
    "name" : "김치",
    "type" : "고춧가루절임",
    "ingredient" : ["배추","고춧가루","소금","고추장","등"],
    "origin" : "대한민국"
    }
ing = input("> 김장할때 재료 : ")
dictionary["ingredient"].append(ing)
#for 반복문 사용
for key in dictionary:
    #출력
    print(key, " : ", dictionary[key])
    
