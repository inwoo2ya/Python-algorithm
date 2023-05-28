import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a_array =[list(map(int,input().split()))for i in range(n)]
m,k = map(int,input().split())
b_array=[list(map(int,input().split()))for i in range(m)]


for i in range(n):
    result = []
    for l in range(k):
        e = 0
        for j in range(m):
            e += a_array[i][j] * b_array[j][l]
        result.append(e)
    print(*result)
