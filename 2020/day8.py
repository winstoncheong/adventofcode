f = open('day8in.txt')
#f = open('testin.txt')
lines = [line.split() for line in f.readlines()]
instructions = [ (line[0], int(line[1])) for line in lines]

def run_program(program):
    """
    Run program given, as a list of tuples.

    Returns a tuple (terminated, accumulator_val)
    """

    acc = 0
    ptr = 0 # index into program
    prev_lines = []

    #print(program)

    while True:

        if ptr >= len(program):
            # Program terminates successfully
            return (True, acc)

        instruction = program[ptr]
        #print(f"Acc: {acc}, Ptr: {ptr}, Instr: {instruction}")

        if ptr in prev_lines:
            # Program infinitely loops
            return (False, acc)

        prev_lines.append(ptr)

        if instruction[0] == 'acc':
            acc += instruction[1]
            ptr += 1
        elif instruction[0] == 'jmp':
            ptr += instruction[1]
        elif instruction[0] == 'nop':
            ptr += 1


print('Ans 1: ', run_program(instructions)[1])

# Part 2

for i, instruction in enumerate(instructions):
    program = []

    if instruction[0] == 'jmp':
        program = instructions[0:i]
        program.append(('nop', instruction[1]))
        program.extend(instructions[i+1:])

    elif instruction[0] == 'nop':
        program = instructions[0:i]
        program.append(('jmp', instruction[1]))
        program.extend(instructions[i+1:])
    

    else:
        continue        
    #print(i, instruction)
    #print(len(instructions), len(program))
    #print(instructions[0:10])
    #print(program[0:10])

    retval = run_program(program)
    #print(i, retval)

    if(retval[0]):
        print('Ans 2: ', retval[1])
