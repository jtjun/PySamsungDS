import math
import traceback

# from wolfram_beta import solve
from sample_complete import solve
from sample_complete import parse_equation

input_path = 'text/input.txt'
output_path = 'text/output.txt'
answer_path = 'text/answer.txt'

solve(input_path, output_path)

def is_same(eq1, eq2, eps=1e-6):
    try:
        t1 = parse_equation(eq1)
    except:
        traceback.print_exc()
        return False
    
    t2 = parse_equation(eq2)

    keys = set(t1.keys()).union(t2.keys())
    for k in keys:
        if not math.isclose(t1.get(k, 0), t2.get(k, 0), rel_tol=eps, abs_tol=eps):
            return False
    
    return True

with open(input_path) as f:
    inputs = f.readlines()

with open(output_path) as f:
    outputs = f.readlines()

with open(answer_path) as f:
    answers = f.readlines()

correct = 0
wrong_cases = []


num = 1
for i, o, a in zip(inputs, outputs, answers):
    if is_same(o.strip(), a.strip()):
        correct += 1
    else:
        wrong_cases.append((num, i, o, a))
    
    num += 1

print("Score : " + str(correct) + "/" + str(correct + len(wrong_cases)))

if len(wrong_cases):
    with open('text/wrong_cases.txt', 'w') as f:
        for num, i, o, a in wrong_cases:
            f.write(
                f'Line #{num}\n' +
                f'Input: {i}' +
                f'Expected: {a}' +
                f'But you : {o}\n'
            )