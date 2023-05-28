import sys

n = int(sys.stdin.readline())
tipList =[]

for _ in range(n):
    t = int(sys.stdin.readline().strip())
    (tipList.append(t))
tipList.sort(reverse=True)

for i in range(n):
    resultTip = tipList[i] -i

    if resultTip < 0 :
        tipList[i] = 0
    else :
        tipList[i] = resultTip

print(sum(tipList))
