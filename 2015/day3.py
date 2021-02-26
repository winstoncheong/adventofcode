f = open('day3in.txt')

line = f.readline()

x = 0
y = 0 
x2 = 0
y2 = 0 

coords = set()
coords.add((x, y))


for c in line:
    if c == '^':
        y += 1
    elif c== 'v':
        y -= 1
    elif c == '<':
        x -= 1
    elif c == '>': 
        x += 1
    coords.add((x,y)) 

print('Ans 1:', len(coords))

# reset for Part 2
x = 0
y = 0
coords = set()
coords.add((x, y))

# Part 2
for n,c in enumerate(line):
    if n % 2 == 0:
        if c == '^':
            y += 1
        elif c== 'v':
            y -= 1
        elif c == '<':
            x -= 1
        elif c == '>': 
            x += 1
        coords.add((x,y)) 
    else:
        if c == '^':
            y2 += 1
        elif c== 'v':
            y2 -= 1
        elif c == '<':
            x2 -= 1
        elif c == '>': 
            x2 += 1
        coords.add((x2,y2)) 

print('Ans 2:', len(coords))