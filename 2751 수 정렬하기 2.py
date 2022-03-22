def merge_sort(m) :
    if len(m)<= 1 :
        return m
    
    mid = len(m)//2
    left = merge_sort(m[:mid])
    right = merge_sort(m[mid:])
    k = 0 #정렬된 리스트 크기
    i = 0 #left
    j = 0 #right
    m = []
    
    while (i<len(left) and j<len(right)) : 
        if left[i] > right[j] : #왼쪽 리스트에서 오른쪽 리스트보다 큰 값이 있을 때
            m[k] = right[j]
            j+= 1
        else :
            m[k] = left[i] # 오른쪽 리스트에서 왼쪽 리스트보다 큰 값이 있을 때
            i+= 1
        k+= 1
        
    if i == len(left) : # 왼쪽에 값을 뽑아서 다 정렬했을 때
        while j < len(right) :
            m[k] = right[j]
            j+=1
            k+=1
    elif j == len(right) : #오른쪽에 값을 뽑아서 다 정렬했을 때
        while i < len(left) :
            m[k]= left[i]
            i+=1
            k+=1
            
    return m
            
        
n = int(input())
m = []
for i in range(n):
    num = int(input())
    m.append(num)

array = merge_sort(m)

for i in array:
    print(i)
