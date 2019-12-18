"""
tower of hanoi
"""
from hanoi_play import play_hanoi
A, B, C = list(), list(), list()
hanoi = [A, B, C]
n = 0
def printHanoi():
    for pole in range(3):
        print(str(pole)+' '+str(hanoi[pole]))

    # error check
    for pole in range(3):
        for i in range(len(hanoi[pole]) - 1):
            if hanoi[pole][i] < hanoi[pole][i + 1]:
                print("\n잘못 이동 되었습니다.\n프로그램을 종료합니다.")
                exit(0)


n = int(input("원판의 수를 입력하세요. : "))

# n 부터 내림차순으로 A 기둥에 원판을 넣으세요.
# A += list(range(n,0,-1))
for i in range(n):
    A.append(n-i)
# 하노이 탑 출력
printHanoi()

"""
play_hanoi 함수를 통해서 전체 정답을 구해야 함
"""

# B 기둥으로 모두 옮겨졌는지 확인, 아니라면 계속 진행
for """ 반복문을 적절하게 설계하기 """:
    """
    # fromPole 과 toPole 을 매 시행마다 받아야 함 
    """
    fromPole =
    toPole =
    print('move from',fromPole,'to',toPole)

    # 적절한 input 인지 체크
    if (fromPole in range(3)) and (toPole in range(3)):
        if len(hanoi[fromPole]) < 1:
            print("잘못된 입력 입니다.")
        else:
            # 적절한 input 이라면 옮김
            block = hanoi[fromPole].pop()
            hanoi[toPole].append(block)
            # hanoi[toPole].append(hanoi[fromPole].pop())

        # 매번 하노이 탑을 출력함
        printHanoi()
    else:
        # 아니라면, 다음 input 받음
        print("잘못된 입력 입니다.")

if len(B) == n:
    print("성공입니다!")
else:
    print('실패입니다.')