"""
tic-tac-toe
game
"""
board = list(range(1, 10))
# 처음 보드 상태 출력함
for i in range(3):
    print(str(board[i*3]) + "|" + str(board[i*3 + 1]) + '|' + str(board[i*3 + 2]))

mark = ['X', 'O']
player = 0
endG = [['X']*3, ['O']*3] # 종료 경우는 O 또는 X 가 세 개 연속
for i in range(9): # 9 번만 input 을 받음
    x = int(input("\n칸 번호 "+mark[player]+" : ")) - 1
    # list index 는 0 부터 시작하므로 1 감소

    # 이미 마킹 되어 있는지 체크
    if board[x] not in mark:
        board[x] = mark[player]
        player = (player+1) % 2
    else:
        # 입력을 새로 받아야 함
        print("잘못된 입력입니다.")

    # 보드를 출력함
    for i in range(3):
        print(str(board[i*3]) + "|" + str(board[i*3 + 1]) + '|' + str(board[i*3 + 2]))

    # condition 체크
    for i in range(3):
        if(([board[i*3], board[i*3 + 1], board[i*3 + 2]] in endG) or # 가로
           ([board[i], board[i + 3], board[i + 6]] in endG) or # 세로
           (i != 1 and [board[0 + i], board[4], board[8 - i]] in endG)): # 대각선 체크
            break

print("게임 종료!")
