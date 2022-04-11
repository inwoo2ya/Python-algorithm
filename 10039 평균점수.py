m = []
for i in range(5):
    n = int(input())
    if n<40 :
        n = 40
        
    m.append(n)

print(sum(m)//5)
