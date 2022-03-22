n = int(input())
m =[]
for i in str(n) :
    m.append(int(i))

m.sort(reverse=True)

for j in m:
    print(j,end="")
