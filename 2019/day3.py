

def path2coords(path):
    """Given path as a string, return a set containing all coordinates in the path"""

    parts = path.split(',')
    coords = list()
    x=0
    y=0

    for part in parts:
        length = int(part[1:])
        # print(length)
        if part[0] == 'D':
            for i in range(length):
                coords.append(f"{x},{y - i - 1}")
            y = y - length
        elif part[0] == 'U':
            for i in range(length):
                coords.append(f"{x},{y + i + 1}")
            y = y + length
        elif part[0] == 'L':
            for i in range(length):
                coords.append(f"{x - i - 1},{y}")
            x = x - length
        elif part[0] == 'R':
            for i in range(length):
                coords.append(f"{x + i + 1},{y}")
            x = x + length
        else:
            pass

    return coords


#coords1 = path2coords('R8,U5,L5,D3')
#coords2 = path2coords('U7,R6,D4,L4')
# coords1 = path2coords('R75,D30,R83,U83,L12,D49,R71,U7,L72')
# coords2 = path2coords('U62,R66,U55,R34,D71,R55,D58,R83')

def taxi(str):
    pair = str.split(',')
    return abs(int(pair[0])) + abs(int(pair[1]))

def min_dist(lst):
    return min(map(taxi, lst))

def timed_dist(lst1, lst2, loc):
    return lst1.index(loc) + lst2.index(loc) + 2

def min_timed_dist(lst1, lst2):
    intersect = set(lst1).intersection(lst2)
    return min(map(lambda y: timed_dist(lst1,lst2,y), intersect))



f = open('day3in.txt','r')
coords1 = path2coords(f.readline())
coords2 = path2coords(f.readline())

intersect = set(coords1).intersection(coords2)
#print(intersect)
print(f'Answer 1: {min_dist(intersect)}')
print(f'Answer 2: {min_timed_dist(coords1, coords2)}')
