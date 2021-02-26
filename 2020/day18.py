import functools
import operator

def tokenize(expr_str):
    """String to list of string-tokens"""
    token_list = filter(lambda x: x != ' ', list(expr_str))
    return list(token_list)

def split_to_ops(expr_lst):
    for i in range(0, len(expr_lst), 2):
        yield expr_lst[i:i+2]

def simple_calc1(expr_lst):
    """Assumes no parentheses in expression-list.
    Part 1:
    Addition and multiplication have same precedence.
    """

    val = int(expr_lst[0])
    # print(list(split_to_ops(expr_lst[1:])))
    for op in split_to_ops(expr_lst[1:]):
        if op[0] == '+':
            val += int(op[1])
        if op[0] == '*':
            val *= int(op[1])

    return val 

def simple_calc2(expr_lst):
    """Assumes no parentheses in expression-list.
    Part 2: 
    Addition before multiplication
    """
    
    # deal with multiplications

    while '+' in expr_lst:
        i = expr_lst.index('+')
        # print(f'Before: {expr_lst}')
        expr_lst[i-1:i+2] = [int(expr_lst[i-1]) + int(expr_lst[i+1])]
        # print(f'After: {expr_lst}')

    # only multiplications left
    vals = map(int, filter(lambda x: x != '*', expr_lst))
    product = functools.reduce(operator.mul, vals)
    return product
    

def calc(expr_lst, simple_calc):
    """Evaluate expression list using new math rules
        simple_calc is a lambda for how to compute. 
        That way this method can be used for parts 1 and 2.
    """

    # Possible exprs
    # d + d
    # d * d
    # d + (..)
    # d * (..)
    # (...)

    # Reduce parens first?

    if '(' not in expr_lst:
        # expression only involves adding and multiplying. Can just compute
        return simple_calc(expr_lst)
    
    else:
        # Find matching closing paren, extract the subexpression, evaluate, and reduce the expression list

        start = expr_lst.index('(')
        depth = 0
        end = -1

        for i, c in enumerate(expr_lst[start:]):
            if c==')':
                depth -= 1
            if c=='(':
                depth += 1
            if depth == 0:
                end = i + start
                break
        
        subexpr = expr_lst[start+1:end]
        # print(f'Found subexpression {subexpr}')
        sub_result = calc(subexpr, simple_calc)
        # print(f'Subresult: {sub_result}')

        # Replace the subexpression with its evalaution
        # print(f'Expression before: {expr_lst}')
        expr_lst[start:end+1] = [sub_result]
        # print(f'Expression after:{expr_lst}')

        # Recurse for if there are additional parens
        return calc(expr_lst, simple_calc)

def calc1(expr_lst):
    """to make mapping over easier"""
    return calc(expr_lst, simple_calc1)

def calc2(expr_lst):
    """to make mapping over easier"""
    return calc(expr_lst, simple_calc2)

## Tests
# expr = '1 + 2 * 3 + 4 * 5 + 6'.split(' ')
# print(calc1(expr))

# expr = tokenize('1 + (2 * 3) + (4 * (5 + 6))')
# print(calc1(expr))

# expr = tokenize('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
# print(calc1(expr))

# expr = tokenize('1 + (2 * 3) + (4 * (5 + 6))')
# print(calc2(expr))

# expr = tokenize('1 + 2 * 3 + 4 * 5 + 6')
# print(calc2(expr))


## input file

f = open('day18in.txt')
lines = [line.strip() for line in f.readlines()]

print('Ans 1: ', sum(map(calc1, [tokenize(line) for line in lines])))
print('Ans 2: ', sum(map(calc2, [tokenize(line) for line in lines])))


