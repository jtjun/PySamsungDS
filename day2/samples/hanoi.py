"""
tower of hanoi
"""
# 아래는 하노이 탑을 출력하기 위한 코드 입니다.
# 신경쓰지 않으셔도 됩니다. (수정하지 마세요.)
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

"""
아래 부분에 input을 받아
n 개의 원판이 있는 하노이 탑을 만드세요.

0 [n, n-1, ..., 2, 1]
1 []
2 []
꼴로 출력 되어야 합니다.
"""
n = int(input("원판의 수를 입력하세요. : "))

# n 부터 내림차순으로 A 기둥에 원판을 넣으세요.
# A += list(range(n,0,-1))
for i in range(n):
    A.append(n-i)
# 하노이 탑 출력
printHanoi()

"""
기둥 이름 두 개를 input 으로 받아
첫 번째 기둥에서 두 번째 기둥으로
원판을 옮기는 과정을
모든 원판이 옮겨질 떄까지 반복하세요.
"""

ans = A.copy()
# B 기둥으로 모두 옮겨졌는지 확인, 아니라면 계속 진행
while B != ans:  # and C != ans:
    fromPole = int(input("\n첫 번째 기둥 (0, 1, 2) : "))
    toPole = int(input("두 번째 기둥 (0, 1, 2) : "))

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

print("성공입니다!")
