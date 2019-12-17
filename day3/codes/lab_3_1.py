def convert(color_code):
    """
    :param color_code: 10진수 또는 16진수 색상 코드 (str)
    :return: 반대 버전의 색상 코드 (str)
    """
    # WRITE YOUR CODE HERE!
    return "#000000"


# DON'T MIND THE CODE BELOW. IT IS JUST FOR TEST.
import pickle
from os.path import abspath, join, dirname

test_file_dir = abspath(join(dirname(__file__), '../tests'))
test_file_path = join(test_file_dir, 'lab_3_1.pkl')

correct = 0
wrong_cases = []

with open(test_file_path, 'rb') as f:
    for x, y in pickle.load(f):
        y_hat = convert(x)
        if y_hat == y:
            correct += 1
        else:
            wrong_cases.append((x, y, y_hat))

total = correct + len(wrong_cases)
print(f"Score: {correct}/{total}")

if len(wrong_cases):
    print("\nWrong Cases:")
    for x, y, y_hat in wrong_cases[:10]:
        print(f"convert('{x}') should be '{y}', not '{y_hat}'")
