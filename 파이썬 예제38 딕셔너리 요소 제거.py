#딕셔너리를 선언합니다.
dictionary = {
    "name" : "건조망고",
    "type" :"당절임"
    }
# 요소 제거전에 내용을 출력
print("요소 제거 이전: ", dictionary)

# 딕셔너리의 요소를 제거
del dictionary["name"]
del dictionary["type"]

# 요소 제거 후에 내용을 출력해 봅니다.
print("요소 제거 이후:",dictionary)
