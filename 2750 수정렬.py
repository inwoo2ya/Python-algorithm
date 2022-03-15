n = int(input())
a = []
for i in range(n) :
    s = int(input())
    a.append(s)

a =  sorted(a,reverse=False)

for j in a :
    print(j)
