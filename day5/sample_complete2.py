import traceback
import math


def print_term(degree, factor):
    if degree == 0: # constant
        return str(factor)
    else: # degree != 0
        if factor == 0:
            return '0'
        term_str = ''
        term_str += str(factor) if abs(factor) != 1 else '-' if factor == -1 else ''
        if type(degree) is str: # cos sin exp
            term_str += degree
        else:
            term_str += 'x^' + str(degree) if degree != 1 else 'x'
        return term_str


def print_equation(terms):
    equation = ''
    for degree, factor in terms.items():
        equation += print_term(degree, factor) + ' + '
    return equation[:-3]  # truncate last ' + '


def parse_term(term_str):
    if 'x' in term_str: # not constant
        factor, degree = '', ''
        if '^' in term_str:
            factor, degree = term_str.split('x^')
            degree = float(degree)
        elif '(' in term_str: # cos(x), sin(x), exp(x)
            factor = term_str[:term_str.find('(') - 3]
            degree = term_str[term_str.find('(') - 3:]
        else: # only x
            factor = term_str.split('x')[0]
            degree = 1
        factor = -1 if factor == '-' else 1 if factor == '' else factor
        return degree, float(factor)

    else: # constant
        return 0, float(term_str)


def parse_equation(equation):
    terms = dict()
    term_str_list = equation.split(' + ')
    for term_str in term_str_list:
        term = parse_term(term_str.strip())
        terms[term[0]] = terms.get(term[0], 0) + term[1]
    return terms


def d_dx_as_terms(terms):
    dterms = dict()
    for degree, factor in terms.items():
        ddegree, dfactor = None, None
        if type(degree) is str:
            dfactor = -factor if degree == 'cos(x)' else factor
            ddegree = 'sin(x)' if degree == 'cos(x)' else 'cos(x)' if degree == 'sin(x)' else 'exp(x)'
        else:
            dfactor = factor * degree
            ddegree = degree - 1
        dterms[ddegree] = dterms.get(ddegree, 0) + dfactor

    return dterms


def d_dx(equation):
    terms = parse_equation(equation)
    dterms = d_dx_as_terms(terms)
    return print_equation(dterms)


def integral_as_terms(terms, constant):
    iterms = dict()
    for degree, factor in terms.items():
        idegree, ifactor = None, None
        if type(degree) is str:
            ifactor = -factor if degree == 'sin(x)' else factor
            idegree = 'cos(x)' if degree == 'sin(x)' else 'sin(x)' if degree == 'cos(x)' else 'exp(x)'
        else:
            idegree = degree + 1
            ifactor = factor / idegree
        iterms[idegree] = iterms.get(idegree, 0) + ifactor

    iterms[0] = iterms.get(0, 0) + constant
    return iterms


def integral(equation, constant):
    terms = parse_equation(equation)
    iterms = integral_as_terms(terms, float(constant))
    return print_equation(iterms)


def compute_as_terms(terms, x):
    result = 0.0
    for degree, factor in terms.items():
        p_result = None # partial result
        if degree == 'cos(x)':
            p_result = math.cos(x)
        elif degree == 'sin(x)':
            p_result = math.sin(x)
        elif degree == 'exp(x)':
            p_result = math.exp(x)
        else:
            p_result = x ** degree
        result += factor * p_result # accumulate
    return result


def compute(equation, x):
    terms = parse_equation(equation)
    return str(compute_as_terms(terms, x))


def solve_query(line):
    try:
        query = line.split(',')
        if query[0] == 'D':
            return d_dx(query[1])
        elif query[0] == 'I':
            return integral(query[1], query[2])
        elif query[0] == 'C':
            return compute(query[1], float(query[2]))
        else:
            return 'ERROR'
    except:
        traceback.print_exc()
        return ''


def solve(input_path, output_path):
    with open(input_path, 'r') as fr:
        with open(output_path, 'w') as fw:
            for line in fr:
                fw.write(solve_query(line) + '\n')

