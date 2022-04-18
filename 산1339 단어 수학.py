n = int(input())
AL_dic ={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0}
AL_list =[]
result=0
pocket=[]

for i in range(n):
    r=input()
    pocket.append(r)
for al in pocket:
    for i in range(len(al)):
        num = 10**(len(al)-i-1)
        AL_dic[al[i]]+=num
        
for j in AL_dic.values():
    if j>0:
        AL_list.append(j)

sorted_list = sorted(AL_list,reverse=True)
for i in range(len(sorted_list)) :
    result += sorted_list[i] * (9-i)

print(result)
