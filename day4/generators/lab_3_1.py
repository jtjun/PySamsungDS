import pickle
import random
import sys
from os.path import abspath, join, dirname

sys.path.append(abspath(join(dirname(__file__), '..')))
from samples.lab_3_1 import convert

test_file_dir = abspath(join(dirname(__file__), '../tests'))
test_file_path = join(test_file_dir, 'lab_3_1.pkl')

with open(test_file_path, 'wb') as f:
    special_cases = [
        '#c0ffee',
        '#000000',
        '#ffffff',
        '#010101',
        '#636465',
    ]

    test_cases = []

    for sc in special_cases:
        y = convert(sc)
        test_cases.append((sc, y))
        test_cases.append((y, convert(y)))

    normal_case_count = 95

    for _ in range(normal_case_count):
        rgb = [str(random.randint(0, 255)) for _ in range(3)]
        x = f"rgb({','.join(rgb)})"
        y = convert(x)
        test_cases.append((x, y))
        test_cases.append((y, x))

    pickle.dump(test_cases, f)
    print(f"{test_file_path} generated!")
