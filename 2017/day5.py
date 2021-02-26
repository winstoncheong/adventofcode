
def run_code(part):
    """limit code reuse"""
    
    with open('day5input.txt') as f:
        lines = f.readlines()
        lines = [int(line.strip()) for line in lines]

    steps = 0
    pos = 0

    while 0 <= pos < len(lines):
        nextpos = pos + lines[pos]
        if part == 1: # part 1: just increment
            lines[pos] += 1
        elif part == 2: # part 2: decrement if offset >=3
             lines[pos] += (-1 if lines[pos] >= 3 else 1)
            
        pos = nextpos
        
        steps += 1


    print(f'Answer {part}: {steps}')

run_code(1)
run_code(2)
