def print_term(factor, degree):
    """
    :param factor: 항의 계수 (int)
    :param degree: 항의 차수 (int, 음이 아닌 정수)
    :return: (str)
    """
    f, d = factor, degree
    term = ""

    if f < 0:
        term += "-"
    if not (abs(f) == 1 and d != 0):
        term += str(abs(f))
    if d > 0:
        term += "x"
    if d > 1:
        term += "^" + str(d)
    return term


def print_equation(terms):
    """
    :param terms: [factor: int, degree: int] 형식의
    2-list로 구성된 (이중) 리스트
    :return: str
    """
    term_str = []
    for f, d in terms:
        term_str.append(print_term(f, d))
    
    return " + ".join(term_str)


def parse_term(term_str):
    """
    :param term_str: str
    :return: [factor: int, degree: int]로 구성된 2-list
    """

    if "x" in term_str:
        f_str, d_str = term_str.split("x")
        if f_str == "-" or f_str == "":
            f_str += "1"
        
        f = int(f_str)
        d = int(d_str[1:]) if d_str else 1
        return [f, d]
    else:
        return [int(term_str), 0]


def parse_equation(equation):
    """
    :param equation: str
    :return: [factor: int, degree: int] 형식의
    2-list로 구성된 (이중) 리스트
    """
    terms = []
    for term_str in equation.split(" + "):
        terms.append(parse_term(term_str))
    
    return terms


def d_dx_as_terms(terms):
    """
    :param terms: [factor: int, degree: int] 형식의
    2-list로 구성된 (이중) 리스트
    :return: terms와 동일한 형식이되,
    그 값이 terms의 미분인 것
    """
    derivative = []

    for f, d in terms:
        if d > 0:
            derivative.append([f * d, d - 1])
    
    if not len(derivative):
        derivative.append([0, 0])
    
    return derivative


def d_dx(equation):
    """
    :param equation: str
    :return: str
    """
    terms = parse_equation(equation)
    terms = d_dx_as_terms(terms)
    return print_equation(terms)


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
