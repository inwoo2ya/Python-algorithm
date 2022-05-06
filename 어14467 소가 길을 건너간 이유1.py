n = int(input())
cow = [None]* 10 #소들의 위치 저장
move = 0 #소가 움직인 횟수
for _ in range(n):
    num, m = map(int,input().split())
    position = cow[num-1] #소들의 현재 위치 저장
    cow[num-1] = m #이번에 입력된 소의 위
    # 소의 위치 None 이 아니면서 이전의 위치와 현재의 위치가 다른지 확인
    if position != None and position != cow[num-1]:
        move +=1
print(move)
