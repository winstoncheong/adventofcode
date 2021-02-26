program = list()
pos = 0

def load_program():
    global program
    f = open('day5in.txt','r')
    
    line = f.readline()
    program = list(map(int,line.split(',')))
    print(program)

def get_param(mode_bits, num):
    global program
    global pos 

    if num==1 and mode_bits[-1] == '1':
        return program[pos+1]
    if num==1 and mode_bits[-1] == '0':
        return program[program[pos+1]]

    if num==2 and mode_bits[-2] == '1':
        return program[pos+2]
    if num==2 and mode_bits[-2] == '0':
        return program[program[pos+2]]

    if num==3 and mode_bits[-3] == '1':
        return program[pos+3]
    if num==3 and mode_bits[-3] == '0':
        return program[program[pos+3]]
    

def run_program():
    global program
    global pos
    pos = 0
    while program[pos] != 99:
        opcode = program[pos]
        mode_bits = "000"
        # print(f"Operation: {opcode}")

        if opcode > 99: # handle modes
            mode_bits = str(opcode)[:-2]
            mode_bits = mode_bits.rjust(3,'0')
            opcode = int(str(opcode)[-2:])
            # print(opcode, mode_bits)

        if opcode == 1: # addition            
            val = get_param(mode_bits, 1) + get_param(mode_bits, 2)
            store = program[pos+3]
            program[store] = val
            # print(f"stored {val} into position {store}")
            pos += 4

        elif opcode == 2: # multiplication
            val = get_param(mode_bits, 1) * get_param(mode_bits, 2)
            store = program[pos+3]
            program[store] = val
            # print(f"stored {val} into position {store}")
            pos += 4

        elif opcode == 3: # input
            val = int(input('>'))
            store = program[pos+1]
            program[store] = val
            pos += 2

        elif opcode == 4: # output
            val = get_param(mode_bits, 1)
            print(val)
            pos += 2
        
        elif opcode == 5: # jump if true
            val = get_param(mode_bits,1)
            if val != 0:
                pos = get_param(mode_bits,2)
            else: 
                pos += 3
        
        elif opcode == 6: # jump if false
            val = get_param(mode_bits,1)
            if val == 0:
                pos = get_param(mode_bits,2)
            else: 
                pos += 3

        elif opcode == 7: # less than
            val1 = get_param(mode_bits, 1)
            val2 = get_param(mode_bits, 2)
            loc = program[pos+3]
            if val1 < val2:
                program[loc] = 1
            else: 
                program[loc] = 0
            pos += 4
        
        elif opcode == 8: # equals
            val1 = get_param(mode_bits, 1)
            val2 = get_param(mode_bits, 2)
            loc = program[pos+3]
            if val1 == val2:
                program[loc] = 1
            else: 
                program[loc] = 0
            pos += 4
        

load_program()
# line = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
# program = list(map(int,line.split(',')))

run_program()        

