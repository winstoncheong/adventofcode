f = open('day7in.txt')

lines = f.readlines()
assigned = {}
rules = []

# methods to manipulate 16bit things (string)
def bin_and(x, y):
    res = ''
    for a, b in zip(x, y):
        if a == '1' and b == '1':
            res += '1'
        else:
            res += '0'
    return res

def bin_or(x, y):
    res = ''
    for a, b in zip(x, y):
        if a == '1' or b == '1':
            res += '1'
        else:
            res += '0'
    return res

def bin_lshift(x, n):
    return x[n:] + "0"*n

def bin_rshift(x, n):
    return '0'*n + x[:-n]

def bin_not(x):
    res = '' 
    for c in x:
        if c=='1':
            res+='0'
        else:
            res+='1'
    
    return res

def convert_to_binstr(n):
    return bin(int(n))[2:].rjust(16, '0')


def load():
    assigned = {}
    rules = []
    # load everything
    for line in lines:
        input, output = list(map(str.strip, line.split('->')))
        inputs = input.split()
        if len(inputs) == 1 and inputs[0].isnumeric(): 
            # found starting numeric assignment
            val = convert_to_binstr(inputs[0])
            assigned[output] = val
            # print(line)

        else:
            rules.append([inputs, output])
    return assigned, rules

def execute(assigned, rules):
    while rules: # end when no more unused rules

        unused = []

        for inputs, output in rules:
            if len(inputs) == 2:
                # command is NOT
                if inputs[1] in assigned:
                    assigned[output] = bin_not(assigned[inputs[1]])
                else:
                    unused.append([inputs, output])
            elif len(inputs) == 3:
                op = inputs[1]
                if op == 'AND' or op == 'OR':
                    arg1 = inputs[0]
                    arg2 = inputs[2]

                    if arg1.isnumeric():
                        in1 = convert_to_binstr(arg1)
                    elif arg1 in assigned:
                        in1 = assigned[arg1]
                    else:
                        # don't have this value
                        unused.append([inputs, output])
                        continue

                    if arg2.isnumeric():
                        in2 = convert_to_binstr(arg2)
                    elif arg2 in assigned:
                        in2 = assigned[arg2]
                    else:
                        # don't have this value
                        unused.append([inputs, output])
                        continue
                    
                    # can apply the AND/OR operation
                    if op == 'AND':
                        assigned[output] = bin_and(in1, in2)
                        # print(f'{in1} and {in2} gave {assigned[output]}')
                    else:
                        assert op == 'OR'
                        assigned[output] = bin_or(in1, in2)
                        # print(f'{in1} or {in2} gave {assigned[output]}')
                elif op == 'LSHIFT' or op == 'RSHIFT':
                    arg1 = inputs[0]
                    arg2 = inputs[2]
                    if arg1 in assigned:
                        # can apply operation
                        in1 = assigned[arg1]
                        in2 = int(arg2)
                        if op == 'LSHIFT':
                            assigned[output] = bin_lshift(in1, in2)
                            # print(f'{in1} lshift {in2} gave {assigned[output]}')
                        else:
                            assert op == 'RSHIFT'
                            assigned[output] = bin_rshift(in1, in2)
                            # print(f'{in1} rshift {in2} gave {assigned[output]}')
                    else:
                        # don't have value
                        unused.append([inputs, output])
                        continue
                else:
                    print(f'Unknown command: {op}')
            elif len(inputs) == 1:
                # this is of the form "symbol -> known_symbol"
                if inputs[0] in assigned:
                    assigned[output] = assigned[inputs[0]]
                else:
                    unused.append([inputs, output])
                
            else:
                print(f'Input with weird number of arguments: {inputs}')
            #print(len(inputs))

        rules = unused
        # print(f'looping with {len(rules)} rules')
    # print(assigned)

assigned, rules = load()
# print(assigned)
execute(assigned, rules)
print(f'Ans 1: {int(assigned["a"], 2)}')

save = assigned["a"]
# reload to reset for ans 2
assigned, rules = load()
assigned['b'] = save
execute(assigned, rules)

print(f'Ans 2: {int(assigned["a"], 2)}')