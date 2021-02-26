from collections import Counter


# x,y => 'L' or '#'
# seats = {}

maxCol = 0
maxRow = 0

def read_in(filename):
    """Read data from filename. Return a dictionary that maps 

    'x,y' -> 'L' or '#'
    
    """
    seats = {}

    # Construct map representation of seating
    f = open(filename)
    lines = f.readlines()

    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if ch=='L':
                seats[str(i)+','+str(j)] = ch

    # data needed for part 2 
    global maxRow
    maxRow = len(lines)
    global maxCol
    maxCol = len(lines[0])


    return seats


def compute_step(seats):
    """
    Compute the changes to be applied. 
    @return a list of coords that will be toggled. 
    """

    coords = [] # coords that will flip

    # determine what seats will change
    for coord,seat in seats.items():
        if seat=='L' and count_occupied(seats, adjacent_coords(seats, coord)) == 0:
            coords.append(coord)

        if seat=='#' and count_occupied(seats, adjacent_coords(seats, coord)) >= 4:
            coords.append(coord)

    return coords


def apply_changes(seats, coord_list):
    """
    Given list of coordinates, flips their state in "seats"
    """
    for coord in coord_list:
        seats[coord] = '#' if seats[coord]=='L' else 'L'

    return seats
        

def count_occupied(seats, coord_list):
    occupied = [ coord for coord in coord_list if seats[coord]=='#' ]
    return len(occupied)



# Return list of adjacent coords
def adjacent_coords(seats, coord):
    """Return list of coords that are adjacent to the coord given. Verify that these coords exist in seats."""

    x,y = coord.split(',')
    adj = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    res = []

    
    for pair in adj:
        nx=pair[0]+int(x)
        ny=pair[1]+int(y)
        nc=str(nx)+','+str(ny)

        if nc in seats.keys():
            res.append(nc)


    return res

def compute_step_part2(seats):
    """
    Compute the changes to be applied for part 2. 
    @return a list of coords that will be toggled. 
    """

    coords = [] # coords that will flip

    # determine what seats will change
    for coord,seat in seats.items():
        if seat=='L' and count_occupied(seats, visible_coords(seats, coord)) == 0:
            coords.append(coord)

        if seat=='#' and count_occupied(seats, visible_coords(seats, coord)) >= 5:
            coords.append(coord)

    return coords

def visible_coords(seats, coord):
    """For part 2. 
    For each direction, find the coordinates of the first seat seen in that direction.
    Return a list of these coords.
    """

    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    ret = []

    for dir in dirs:
        x,y = map(int, coord.split(','))

        # make adjustment
        x+= dir[0]
        y+= dir[1]

        while 0<=x<=maxRow and 0<=y<=maxCol:
            pos = str(x)+','+str(y) 
            if pos in seats.keys():
                ret.append(pos)
                break

            else:
                x+= dir[0]
                y+= dir[1]

    return ret



# ------------
filename='day11in.txt'

# Find answer 1
seats = read_in(filename)
while True:
    changes = compute_step(seats)
    if len(changes) == 0:
        ctr = Counter(seats.values())
        print(ctr)
        print('Answer 1: ', ctr['#'])
        break
    else:
        apply_changes(seats, changes)
        

# Find answer 2
seats = read_in(filename)
while True:
    changes = compute_step_part2(seats)
    if len(changes) == 0:
        ctr = Counter(seats.values())
        print(ctr)
        print('Answer 2: ', ctr['#'])
        break
    else:
        apply_changes(seats, changes)
        


