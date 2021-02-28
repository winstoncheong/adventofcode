from collections import defaultdict
from fractions import gcd
from collections import Counter

import re

f = open('day6in.txt')

lines = f.readlines()

reg = r'(turn on|turn off|toggle) (\d*,\d*) through (\d*,\d*)'

# (x,y) => bool
grid = defaultdict(bool)
grid2 = defaultdict(int)

def rect_of_points(start, stop):
    assert start[0] <= stop[0]
    assert start[1] <= stop[1]
    
    points = []
    
    for i in range(start[0], stop[0]+1):
        for j in range(start[1], stop[1]+1):
            points.append((i,j))

    return points

for line in lines:
    print(line)
    m = re.match(reg, line)
    instruction = m.groups()

    start = list(map(int, instruction[1].split(',')))
    stop = list(map(int, instruction[2].split(',')))

    points = rect_of_points(start, stop)

    for point in points:
        if instruction[0]=='turn off':
            grid[point] = False
            grid2[point] = max(grid2[point]-1, 0) # don't go below zero
        elif instruction[0]=='turn on':
            grid[point] = True
            grid2[point] += 1
        elif instruction[0]=='toggle':
            grid[point] = not grid[point]
            grid2[point] += 2

ctr = Counter(grid.values())

print('Ans 1:', ctr[True])
print('Ans 2:', sum(grid2.values()))