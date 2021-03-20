f = open('day8in.txt')

lines = [line.strip() for line in f.readlines()]

def count_chars(line):
    i = 1
    num = 0
    while i < len(line) - 1:
        if line[i] == '\\':
            if line[i+1] == 'x': # hex excape character
                i += 4
                num += 1
                continue
            else: # normal esape character
                i += 2
                num += 1
                continue
        else:
            i += 1
            num += 1
    return num

def added_chars_to_reencode(line):
    num = 2 # start with the first 2 outer quotes
    for c in line:
        if c=='"' or c=='\\':
            num += 1
    return num
    
print('Ans 1:', sum([len(line) - count_chars(line) for line in lines]))
print('Ans 2:', sum([added_chars_to_reencode(line) for line in lines]))