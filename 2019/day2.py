
program = list()
pos = 0

def load_program(input1, input2):
    global program
    f = open('day2in.txt','r')
    # f = open('test.in','r')

    line = f.readline()
    program = list(map(int,line.split(',')))

    program[1] = input1
    program[2] = input2

def run_program():
    global program
    global pos
    pos = 0
    while program[pos] != 99:
        instr = program[pos]
        if instr == 1: # addition
            val = program[program[pos+1]] + program[program[pos+2]]
            store = program[pos+3]
            program[store] = val
            # print(f"stored {val} into position {store}")

        if instr == 2: # multiplication
            val = program[program[pos+1]] * program[program[pos+2]]
            store = program[pos+3]
            program[store] = val
            # print(f"stored {val} into position {store}")

        pos += 4

load_program(12,2)
run_program()
print(f'Answer 1: {program[0]}')

for i in range(100):
    for j in range(100):
        load_program(i,j)
        run_program()
        if(program[0]==19690720):
            print(f'Answer 2: {i*100+j}')
            break

