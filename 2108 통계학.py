from collections import Counter

n = int(input())
list =[]
if n % 2 == 1 :
    for i in range(n) :
        m = int(input())
        list.append(m)

list.sort()
cnt = Counter(list).most_common()

print(round(sum(list)/n))

print(list[n//2])

if len(cnt) > 1 :
    if cnt[0][1] == cnt[1][1] :
        print(cnt[1][0])
    else :
        print(cnt[0][0])
else :
        print(cnt[0][0])
        
print(max(list)-min(list))
 
