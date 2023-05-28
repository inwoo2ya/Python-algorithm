import sys

n = int(sys.stdin.readline())
result= []
poped_result = 0
for _ in range(n):
    c = int(sys.stdin.readline())
    result.append(c)

result.sort(reverse= True)
for i in range(2,len(result),3):
    poped_result += result[i]

print(sum(result)-poped_result)