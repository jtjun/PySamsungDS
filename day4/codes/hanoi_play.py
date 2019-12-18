# WRITE FUNCTION play_hanoi().
# YOU COULD DEFINE NEW FUNCTION
# OR CHANGE PARAMETERS OF play_hanoi() IF YOU WANT TO.

def play_hanoi(n):
    """
    :param n: 원판의 개수 (int, 양의 정수)
    :return: 0번 기둥에서 1번 기둥으로 이동시키기 위한 움직임
    각각의 움직임은 [시작 기둥: int, 끝 기둥: int]으로 구성되며,
    위와 같은 2-list로 구성된 리스트를 반환한다.
    """
    # WRITE YOUR CODE HERE!
    return [[0, 0]]


# DON'T MIND THE CODE BELOW. IT IS JUST FOR TEST.
n = int(input("원판의 수를 입력하세요. : "))
poles = [[] for _ in range(3)]
complete = list(range(n, 0, -1))
poles[0] = complete.copy()

def print_hanoi():
    for i in range(3):
        print(f"Pole #{i} : {' '.join(map(str, poles[i]))}")

move_count = 0
for idx, move in enumerate(play_hanoi(n)):
    _from, _to = move
    print_hanoi()
    print(f"\n#{idx + 1}: {_from}에서 {_to}로 이동")

    # 적절한 input 인지 체크
    if (_from not in range(3)) or (_to not in range(3)):
        print(": 잘못된 입력, 실행 중단\n")
        break
    
    if not len(poles[_from]):
        print(": 기둥이 비어 있음, 실행 중단\n")
        break

    if len(poles[_to]) and poles[_from][-1] > poles[_to][-1]:
        print(": 더 큰 원판을 집어넣으려 함, 실행 중단\n")
        break

    move_count += 1
    print()
    block = poles[_from].pop()
    poles[_to].append(block)

print_hanoi()
print()

success = poles[1] == complete
print(f"성공 여부 : {success}")
print(f"이동 횟수 : {move_count}")

score = int(success) and (100 * (2 ** n - 1) / move_count)
print(f"점수 : {score:.2f}")
