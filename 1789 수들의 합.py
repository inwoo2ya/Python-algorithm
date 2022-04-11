s = int(input())
sum = 0
n=0
for i in range(1,s+1):
    sum += i
    
    if sum > s:
        n = i-1
        break
    elif s == 1:
        n = 1
print(n)
