import sys
n,m = map(int,sys.stdin.readline().split())
dict_p = {}
answer = []
for i in range(n):
    poketmon = input()
    dict_p[i+1] = poketmon
    dict_p[poketmon] = i+1

for _ in range(m):
    question = input()
    if question.isdigit():
        question = int(question)
        answer.append(dict_p[question])
    else:    
        answer.append(dict_p[question])
for k in answer:
    print(k)
