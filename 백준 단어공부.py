words = input().upper() # 대문자변환
ewords = list(set(words)) # 중복함수 제거
m = 0
for st in ewords :
     sc = words.count(st)
     if sc > m :
         m = sc
         ms = st
     elif ms == st :
         pass
     elif m == sc :
         ms = "?"
         
print(ms)
