def print_term(factor, degree):
    """
    :param factor: 항의 계수 (int)
    :param degree: 항의 차수 (int, 음이 아닌 정수)
    :return: (str)
    """
    # WRITE YOUR CODE HERE
    return "x"


def print_equation(terms):
    """
    :param terms: [factor: int, degree: int] 형식의
    2-list로 구성된 (이중) 리스트
    :return: str
    """
    # WRITE YOUR CODE HERE.
    # ... AND YOU MAY USE THE print_term() ABOVE.
    term_str = []
    return "x"


def parse_term(term_str):
    """
    :param term_str: str
    :return: [factor: int, degree: int]로 구성된 2-list
    """
    # WRITE YOUR CODE HERE.
    return [0, 0]


def parse_equation(equation):
    """
    :param equation: str
    :return: [factor: int, degree: int] 형식의
    2-list로 구성된 (이중) 리스트
    """
    # WRITE YOUR CODE HERE.
    # ... AND YOU MAY USE THE parse_term() ABOVE.
    return [[0, 0]]


def d_dx_as_terms(terms):
    """
    :param terms: [factor: int, degree: int] 형식의
    2-list로 구성된 (이중) 리스트
    :return: terms와 동일한 형식이되,
    그 값이 terms의 미분인 것
    """
    # WRITE YOUR CODE HERE.
    return [[0, 0]]


def d_dx(equation):
    """
    :param equation: str
    :return: str
    """
    # WRITE YOUR CODE HERE.
    # ... AND YOU MAY USE
    # THE parse_term(),
    # THE d_dx_as_terms(),
    # AND THE print_equation()!
    return equation


# DON'T MIND THE CODE BELOW. IT IS JUST FOR TEST.
import pickle
from os.path import abspath, join, dirname

test_file_dir = abspath(join(dirname(__file__), '../tests'))
test_file_path = join(test_file_dir, 'lab_3_4.pkl')


correct = 0
wrong_cases = []

with open(test_file_path, 'rb') as f:
    dataset = pickle.load(f)

for x, y in dataset:
    y_hat = parse_equation(x)
    if y_hat == y:
        correct += 1
    else:
        wrong_cases.append(x)

total = correct + len(wrong_cases)
print(f"parse_equation() Score: {correct}/{total}")

if len(wrong_cases):
    print("\nWrong Cases:")
    for x in wrong_cases[:10]:
        print(f"'{x}'")
    exit(1)


correct = 0
wrong_cases = []
for x, y in dataset:
    by_degree = {}

    for f, d in y:
        if d == 0:
            continue
        
        by_degree[d-1] = by_degree.get(d-1, 0) + f * d
    
    for f, d in parse_equation(d_dx(x)):
        by_degree[d] = by_degree.get(d, 0) - f
    
    if all(map(lambda x: x == 0, by_degree.values())):
        correct += 1
    else:
        wrong_cases.append(x)
    
print(f"d_dx() Score: {correct}/{total}")

if len(wrong_cases):
    print("\nWrong Cases:")
    for x in wrong_cases[:10]:
        print(f"'{x}'")
    exit(1)
