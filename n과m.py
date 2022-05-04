n,m = list(map(int,input().split()))
result =[] # m개의 수열을 저장

def dfs() :
    if len(result) == m:#리스트에 들어간 수열들이 m개가 되면 숫자 모두 출력
        print(" ".join(map(str,result)))
        return
    for i in range(1,n+1):
        if i not in result: #중복여부 확인
            result.append(i) #중복아니면 숫자 i를 리스트에 넣는다.
            dfs() # result = [1]인 상태에서 다음 숫자를 넣기위하여 가지치기
            result.pop() #if n=4, m=2 라면 [1] => [1,2] pop() -> [1] -> [1,3] pop() -> [1]-> [1,4] pop() -> for문 반복 -> [2]->[2,1] pop() ->[2]... 이런식으로 반복

dfs()
