a,b,v = map(int,input().split())
d = a-b
i = 0 #올라가는 데 걸리는 일수
if (v-b) % d !=0 :
    i = ((v-b) // d) +1
    
else :
    i = ((v-b) // d)
print(i)

#v-b 모르겠다.
