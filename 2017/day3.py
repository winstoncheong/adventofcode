
import math

puzzle_input=265149

grid = {}

def keystr(x, y):
    return str(x)+','+str(y)

def generate_grid(num, part):
    """
        part is used specify which grid, because the logic for traversing
        the grid is reused.
    """
    global grid
    grid = {} # clear grid
    size = math.ceil(num**.5) # size of grid
    
    # print(size)

    direction = 'R'
    curr_size = 1 # used to detect how far we should be from origin
    x=0
    y=0
    val = 1
    key = str(x)+','+str(y)

    grid[key] = val

    for i in range(2, size**2+1):
        # do the move
        if direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        elif direction == 'U':
            y += 1
        elif direction == 'D':
            y -=1
        elif direction == 'G': # grow grid
            curr_size += 1
            x += 1
            direction = 'R'
            
            
        # add to dict
        if part==1: # grid value should be i
            val = i
            grid[keystr(x,y)] = val
            
        elif part==2: # populate grid with sum of adjacent values

            val = grid.get(keystr(x-1, y-1), 0) + grid.get(keystr(x-1, y), 0)\
                  + grid.get(keystr(x-1, y+1), 0) + grid.get(keystr(x, y-1), 0)\
                  + grid.get(keystr(x, y+1), 0) + grid.get(keystr(x+1, y-1), 0)\
                  + grid.get(keystr(x+1, y), 0) + grid.get(keystr(x+1, y+1), 0)
                      
            grid[keystr(x,y)] = val
                      
            if val > num: # can stop after this step    
                return
        
        
        # check if we've hit the edge. If so, turn direction
        if direction == 'R' and x == curr_size:
            direction = 'U'
            if y == -curr_size: # detect when in bottom right corner
                direction = 'G' # grow grid
        elif direction == 'U' and y == curr_size:
            direction = 'L'
        elif direction == 'L' and x == -curr_size:
            direction = 'D'
        elif direction == 'D' and y == -curr_size:
            direction = 'R'

def steps(num):
    """How many steps to go from num to 1"""

    for k, v in grid.items():
        if v==num:
            # k is the set of coordinates we are looking for
            # split  ->   int   ->   abs  -> sum
            # "3,-7" -> [3, -7] -> [3, 7] -> 10

            # print(k)
            return sum(map(abs,map(int, k.split(','))))
            
            
    
    
num = puzzle_input
generate_grid(num, 1)
print(f'Answer 1: {steps(num)}')
generate_grid(num, 2)
print(f'Answer 2: {max(grid.values())}')
