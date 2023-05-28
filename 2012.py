import sys
n = int(sys.stdin.readline())
rank_arr = []
for _ in range(n):
    rank_arr.append(int(sys.stdin.readline()))

rank_arr.sort()

#불만족 Sum
result = 0
# i = 1
# j = 0
# while(j < n):
#     result += abs(i-rank_arr[j])
#     i+=1
#     j+=1
for i in range(1,n+1):
    result += abs(rank_arr[i-1]-i)
print(result)