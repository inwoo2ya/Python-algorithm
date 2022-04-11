m = []
for i in range(3):
    n = (input())
    m.append(n)

a = int(m[0])
b = int(m[2])

if m[1] == '+' :
    print(a+b)
elif m[1] == '*' :
    print(a*b)
