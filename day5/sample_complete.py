import math
import traceback


def print_term(degree, factor):
    """
    :param degree: 항의 차수 (int, 음이 아닌 정수)
    :param factor: 항의 계수 (int)
    :return: (str)
    """
    f, d = factor, degree
    term = ""

    if d == "exp(x)":
        return str(factor) + "exp(x)"
    elif d == "sin(x)":
        return str(factor) + "sin(x)"
    elif d == "cos(x)":
        return str(factor) + "cos(x)"

    if f < 0:
        term += "-"
    if not (abs(f) == 1 and d != 0):
        term += str(abs(f))
    if d != 0:
        term += "x"
    if d != 0 and d != 1:
        term += "^" + str(d)
    return term


def print_equation(terms):
    """
    :param terms: dict (key=degree, value=factor)
    :return: str
    """
    term_str = []
    for d, f in terms.items():
        term_str.append(print_term(d, f))
    
    return " + ".join(term_str)


def parse_term(term_str):
    """
    :param term_str: str
    :return: (degree: int, factor: int)
    """
    if term_str.endswith('(x)'):
        d = term_str[-6:]
        f_str = term_str[:-6]
        if f_str == "-" or f_str == "":
            f_str += "1"
        
        return d, float(f_str)
    elif "x" in term_str:
        f_str, d_str = term_str.split("x")
        if f_str == "-" or f_str == "":
            f_str += "1"
        
        f = float(f_str)
        d = float(d_str[1:]) if d_str else 1.0
        return d, f
    else:
        return 0.0, float(term_str)


def parse_equation(equation):
    """
    :param equation: str
    :return: dict (key=degree, value=factor)
    """
    terms = {}
    for term_str in equation.split(" + "):
        d, f = parse_term(term_str)
        terms[d] = terms.get(d, 0) + f
    
    return terms


def d_dx_as_terms(terms):
    """
    :param terms: dict (key=degree, value=factor)
    :return: terms와 동일한 형식이되,
    그 값이 terms의 미분인 것
    """
    derivative = {}

    for d, f in terms.items():
        if d == "sin(x)":
            derivative["cos(x)"] = derivative.get("cos(x)", 0) + f
        elif d == "cos(x)":
            derivative["sin(x)"] = derivative.get("sin(x)", 0) - f
        elif d == "exp(x)":
            derivative["exp(x)"] = derivative.get("exp(x)", 0) + f
        elif d != 0:
            derivative[d - 1] = derivative.get(d - 1, 0) + f * d
    
    if not len(derivative):
        derivative[0] = 0
    
    return derivative


def d_dx(equation):
    """
    :param equation: str
    :return: str
    """
    terms = parse_equation(equation)
    terms = d_dx_as_terms(terms)
    return print_equation(terms)


def integral_as_terms(terms, constant):
    result = {0: constant}
    for d, f in terms.items():
        if d == "sin(x)":
            result["cos(x)"] = result.get("cos(x)", 0) - f
        elif d == "cos(x)":
            result["sin(x)"] = result.get("sin(x)", 0) + f
        elif d == "exp(x)":
            result["exp(x)"] = result.get("exp(x)", 0) + f
        else:
            result[d + 1] = result.get(d + 1, 0) + f / (d + 1)
    
    return result


def integral(equation, constant):
    terms = parse_equation(equation)
    terms = integral_as_terms(terms, constant)
    return print_equation(terms)


def compute_as_terms(terms, x):
    y = 0
    for d, f in terms.items():
        if d == "sin(x)":
            y += f * math.sin(x)
        elif d == "cos(x)":
            y += f * math.cos(x)
        elif d == "exp(x)":
            y += f * math.exp(x)
        else:
            y += f * (x ** d)
    return y


def compute(equation, x):
    terms = parse_equation(equation)
    y = compute_as_terms(terms, x)
    return str(y)


def solve_query(line):
    try:
        tokens = line.split(',')
        command = tokens[0]

        if command == 'D':
            return d_dx(tokens[1])
        elif command == 'I':
            return integral(tokens[1], float(tokens[2]))
        elif command == 'C':
            return compute(tokens[1], float(tokens[2]))
    except:
        traceback.print_exc()
        return ''


def solve(input_path, output_path):
    input_f = open(input_path)
    output_f = open(output_path, 'w')

    for line in input_f:
        line = solve_query(line.strip())
        output_f.write(line + '\n')
    
    input_f.close()
    output_f.close()
