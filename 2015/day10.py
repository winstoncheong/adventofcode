import time

f = open('day10in.txt')
line = f.readline().strip()

def look_say(line):
    i = 0
    out = ''

    while i < len(line):
        c = line[i]
        if len(line) > i+1 and line[i+1] == c:
            if len(line) > i+2 and line[i+2] == c: # c occurs thrice
                out+='3'+c
                i += 3 
                continue
            else: # c occurs twice
                out += '2'+c
                i += 2 
                continue
        else: # c occurs once
            out += '1'+c
            i += 1 
    return out

# start = time.time()
for i in range(40):
    line = look_say(line)
# stop = time.time()
# print('took', stop-start)

print('Ans 1:', len(line))

# start = time.time()
for i in range(10):
    line = look_say(line)
# stop = time.time()
# print('took', stop-start)

print('Ans 2:', len(line))