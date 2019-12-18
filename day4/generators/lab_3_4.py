import pickle
import random
import sys
from os.path import abspath, join, dirname
from pprint import pprint

sys.path.append(abspath(join(dirname(__file__), '..')))
from samples.lab_3_4 import print_equation

test_file_dir = abspath(join(dirname(__file__), '../tests'))
test_file_path = join(test_file_dir, 'lab_3_4.pkl')

# 차원
# term 개수
#   각 항 별로 테케 하나씩
#   항 2개 조합한걸로도 테케 똑같은 개수만큼
#   항 3~10개 사이 랜덤으로 똑같은 개수만큼
# 계수
#   -2 -1 0 1 2 반드시 포함
#   이외 정수도 반드시 포함 (양수 & 음수)
#   범위는... 적당히 1000까지~
# 차수
#   0 1 2 3+
#   범위는... 마찬가지로 1000까지~

F = 6   # F 이상 = 많다
D = 6   # D차항 이상 = 많다

terms = []
for _d in range(D + 1):
    for _f in range(-F, F + 1):
        if _d == D:
            d = random.randint(3, 1000)
        else:
            d = _d
        
        if abs(_f) == F:
            f = _f * random.randint(1, 500)
        else:
            f = _f
        
        terms.append([[f, d]])

def draw():
    return random.choice(terms)[0]

case_size = len(terms)


multiple_terms = []
for _ in range(case_size):
    multiple_terms.append([
        draw(),
        draw()
    ])

    multiple_terms.append([
        draw()
        for _ in range(random.randint(3, 10))
    ])

terms.extend(multiple_terms)


with open(test_file_path, 'wb') as f:
    pickle.dump([
        (print_equation(t), t)
        for t in terms
    ], f)
