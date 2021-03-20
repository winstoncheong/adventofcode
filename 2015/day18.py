from pprint import pprint


f = open('day18in.txt')
# f = open('test.txt')
lines = f.readlines()
grid = [list(line.strip()) for line in lines]
SIZE = 100

def neighbor_coords(i, j):
    """Assumes grid limits are 0--SIZE exclusive"""
    coords = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x==0 and y == 0:
                continue
            if 0 <= x+i < SIZE and 0 <= y+j < SIZE:
                coords.append((x+i, y+j))
    return coords

def count_neighbors_on(grid, i, j):
    count = 0
    coords = neighbor_coords(i, j)
    for coord in coords:
        if grid[coord[0]][coord[1]] == '#': 
            count += 1
    return count

def step(grid):
    newgrid = []

    for i in range(SIZE):
        newrow = []
        for j in range(SIZE):
            on = count_neighbors_on(grid, i, j)
            if grid[i][j] == '#':
                if  on == 2 or on == 3:
                    newrow.append('#')
                else:
                    newrow.append('.')
            else: # this position is off
                if on == 3:
                    newrow.append('#')
                else:
                    newrow.append('.')
        newgrid.append(newrow)
    return newgrid

def count_all_on(grid):
    count = 0
    for row in grid:
        for c in row:
            if c == '#':
                count += 1
    return count

for i in range(100):
    grid = step(grid)

print('Ans 1:', count_all_on(grid))

# Part 2

# reload
grid = [list(line.strip()) for line in lines]
corners = [(0,0), (0, SIZE-1), (SIZE-1, 0), (SIZE-1, SIZE-1)]
# turn corners on
for coord in corners:
    grid[coord[0]][coord[1]] = '#'

for i in range(100):
    grid = step(grid)
    # turn corners on
    for coord in corners:
        grid[coord[0]][coord[1]] = '#'

print('Ans 2:', count_all_on(grid))