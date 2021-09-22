character = {
    "name" : "김지인",
    "level" : "22",
    "items" : {
        "weapon" : "갤럭시 S10 5G",
        "armor" : "퓨마 롱패딩"
        },
    "skill" : ["트름하기","고성방가","춤추기"]
    }

for key in character :
    if type(character[key]) is dict :
        for small_key in character[key] :
            print(small_key , ":" ,character[key][small_key])
    elif type(character[key]) is list :
        for item in character[key] :
            print(key,":",item)
    else :
        print(key,":",character[key])
