n = int(input())
m=[]
for i in range(n):
    age,name = (input().split())
    age = int(age)
    m.append((age, name))
    
m.sort(key=lambda x:x[0])

for j in m:
    print(j[0], j[1])
