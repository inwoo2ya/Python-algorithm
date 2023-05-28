import sys
n,k = map(int,sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
left,right = 0, 0

counter = [0]* (max(array) + 1)
answer = 0
while right < n :
    if counter[array[right]] < k:
        counter[array[right]] +=1
        right += 1
    else:
        counter[array[left]] -= 1
        left += 1
    answer = max(answer, right - left)
print(answer)