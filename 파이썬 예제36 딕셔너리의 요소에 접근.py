#딕셔너리 선언
dictionary = {
    "name" : "짜오네중국집",
    "type" : "League of Legend",
    "position" : ["top","mid","jungle"],
    "origin" : "쉔"
    }
#출력
print("name : ",dictionary["name"])
print("type : ", dictionary["type"])
print("position : ",dictionary["position"])
print("주챔: " ,dictionary["origin"])
print()

#값을 변경

dictionary["name"] = "다룽아"
print("name : " ,dictionary["name"])
