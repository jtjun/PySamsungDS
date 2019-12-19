def convert(color_code):
    """
    :param color_code: 10진수 또는 16진수 색상 코드 (str)
    :return: 반대 버전의 색상 코드 (str)
    """
    if color_code[0] == "#":
        r = int(color_code[1:3], 16)
        g = int(color_code[3:5], 16)
        b = int(color_code[5:7], 16)
        return "rgb(%d,%d,%d)" % (r, g, b)
    else:
        r, g, b = color_code[4:-1].split(",")
        return "#%02x%02x%02x" % (int(r), int(g), int(b))


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
