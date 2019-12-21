"""
tic-tac-toe
game
"""
board = [list(range(1, 4)), list(range(4, 7)), list(range(7, 10))]
# board = [[1,2,3], [4,5,6], [7,8,9]]
# 처음 보드 상태 출력함
for line in board:
    print(str(line[0]) + "|" + str(line[1]) + '|' + str(line[2]))

mark = ['X', 'O']
player = 0
condition = 1
while condition:
    x = int(input("\n칸 번호 "+mark[player]+" : "))
    x -= 1 # list index 는 0 부터 시작하므로 1 감소

    # 이미 마킹 되어 있는지 체크
    if board[x//3][x%3] not in mark:
        board[x//3][x%3] = mark[player]
        player = (player+1) % 2
        condition += 1 # 1 씩 증가 (올바른 input 경우에만)
    else:
        # 입력을 새로 받아야 함
        print("잘못된 입력입니다.")

    # 보드를 출력함
    for line in board:
        print(str(line[0]) + "|" + str(line[1]) + '|' + str(line[2]))

    # condition 체크
    if condition > 9:
        break  # 9번째 입력을 받으면 더이상 입력을 받을 수 없음

    for i in range(3):
        if((board[i][0] == board[i][1] == board[i][2]) or # 가로
           (board[0][i] == board[1][i] == board[2][i]) or # 세로
           (i != 1 and (board[0][i] == board[1][1] == board[2][2-i]))): # 대각선
            condition = 0

print("게임 종료!")
