from collections import defaultdict

# f = open('testin.txt')
f = open('day17in.txt')
lines = [line.strip() for line in f.readlines()]

# (x,y,z) => bool
grid = defaultdict(bool)
grid2 = defaultdict(bool) # for part 2


for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c=='#':
            grid[(i,j,0)] = True
            grid2[(i,j,0,0)] = True
        else:
            grid[(i,j,0)] = False
            grid2[(i,j,0,0)] = False

# print(grid)


def adjacents(coord):
    """Make this work for parts 1 and 2. Allows reusage of other functions"""
    adj = []

    if len(coord) == 3:
        adj = [(coord[0]+i, coord[1]+j, coord[2]+k) for i in range(-1, 2) for j in range(-1, 2) for k in range(-1, 2)]
    if len(coord) == 4:
        adj = [(coord[0]+i, coord[1]+j, coord[2]+k, coord[3]+n) for i in range(-1, 2) for j in range(-1, 2) for k in range(-1, 2) for n in range(-1, 2)]

    adj.remove(coord)
    return adj

def count_active_adjacent(grid, coord):
    """Works for both parts 1 and 2"""
    adjs = adjacents(coord)
    return sum([grid[adj] for adj in adjs])

def potential_coords(grid):
    """Get coordinates that potentially matter for updating the given grid state
    Works for both parts 1 and 2
    """

    active_coords = [k for k,v in grid.items() if v]
    potential_coords = set(active_coords)

    for coord in active_coords:
        adjs = adjacents(coord)
        potential_coords = potential_coords.union(adjs)

    return potential_coords


def step(grid):
    """Return new grid state after executing a step"""
    coords = potential_coords(grid)
    next_grid = defaultdict(bool)
    for coord in coords:
        if grid[coord]: # active
            c= count_active_adjacent(grid, coord)
            if c == 2 or c == 3:
                next_grid[coord] = True
            else:
                next_grid[coord] = False 
        else: # inactive
            c= count_active_adjacent(grid, coord)
            if c==3: 
                next_grid[coord] = True
            else:
                next_grid[coord] = False

    return next_grid

def print_grid(grid):
    '''Prints grid for debugging'''
    active_coords = [k for k,v in grid.items() if v]

    minZ = min(c[2] for c in active_coords)
    maxZ = max(c[2] for c in active_coords)
    minX = min(c[0] for c in active_coords)
    maxX = max(c[0] for c in active_coords)
    minY = min(c[1] for c in active_coords)
    maxY = max(c[1] for c in active_coords)

    for i in range(minZ, maxZ + 1):
        print(f'Z = {i}')
        for j in range(minX, maxX+1):
            for k in range(minY, maxY+1):
                c = '#' if grid[(j, k, i)] else '.'
                print(c,end='')
            print('')

        print('')

def boot(grid):
    """Boot process is six cycles. return grid state after"""

    for i in range(6):
        grid = step(grid)
    
    return grid

booted = boot(grid)
print('Ans 1:', sum(booted.values()))

booted2 = boot(grid2)
print('Ans 2:', sum(booted2.values()))