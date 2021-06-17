
import re
from collections import defaultdict

f = open('day8input.txt')
lines = f.readlines()
pattern = r'^(\w*) (inc|dec) (-?\d*) if (\w*) (>=|>|<|<=|!=|==) (-?\d*)$'
prog = re.compile(pattern)

var_dict = defaultdict(int)
cond_dict = {
        '<=' : lambda x, y: x <= y,
        '>=' : lambda x, y: x >= y,
        '<' : lambda x, y: x < y,
        '>' : lambda x, y: x > y,
        '==' : lambda x, y: x == y,
        '!=' : lambda x, y: x != y
    }

max_ever = 0

def eval_conditional(conditional):
    fct = cond_dict[conditional[1]]
    return fct(var_dict[conditional[0]], int(conditional[2]))

def eval_expression(expression):
    global max_ever
    
    if expression[1] == 'inc':
        var_dict[expression[0]] += int(expression[2])
    else:    
        assert expression[1] == 'dec'
        var_dict[expression[0]] -= int(expression[2])

    # addon for part 2
    # do for both ops since can decrement by a negative
    max_ever = max(max_ever, var_dict[expression[0]])

# Runs the program 
for line in lines:
    matched = prog.match(line)
    assert matched # pattern should match all lines of input
    
    expression = matched.group(1,2,3)
    conditional = matched.group(4,5,6)

    # print(expression, conditional)
    
    if eval_conditional(conditional):
        eval_expression(expression)
    

print(f'Answer 1: {max(var_dict.values())}')
print(f'Answer 2: {max_ever}')
