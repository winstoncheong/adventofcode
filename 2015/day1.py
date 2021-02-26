from collections import Counter

f = open('day1input.txt')
line = f.readline()

ctr = Counter(line)
print('Ans 1: ', ctr['('] - ctr[')'])

floor = 0
for n, c in enumerate(line):
    if c == '(':
        floor += 1
    elif c== ')':
        floor -= 1
        if floor == -1:
            print('Ans 2: ', n+1)
            break