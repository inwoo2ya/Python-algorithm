n, m = map(int,input().split())
chessBoard = []
for _ in range(n):
    chessBoard.append(input())

for i in range(n-7): 
    for j in range(m-7): # 8x8 크기의 체스판을 검사할 것 때문에 => 전체 보드판을 벗어나지 않기위함
        d1 = 0
        d2 = 0
print(chessBoard)