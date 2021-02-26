import re
import collections

class Rect:
    def __init__(self, x=-1, y=-1, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def hasPoint(self, a, b):
        return self.x <= a <= self.x + self.w - 1 and \
                self.y <= b <= self.y + self.h - 1
    

regex = r'#\d* @ (\d*),(\d*): (\d*)x(\d*)'

f = open('day3in.txt','r')
# f = open('testin.txt','r')

lines = f.readlines()
rects = []

for line in lines:
    m = re.search(regex, line)
    x = int(m.group(1))
    y = int(m.group(2))
    width = int(m.group(3))
    height = int(m.group(4))

    # print(f'x:{x}, y:{y}, width:{width}, height:{height}')
    rects.append(Rect(x, y, width, height))

# print(rects)

maxX = max([rect.x + rect.w for rect in rects])
maxY = max([rect.y + rect.h for rect in rects])

print("Num rects:", len(rects))
print("maxX:", maxX)
print("maxY:", maxY)

# Try making a dict: (pixel) => rect_count
# that counts coverage for each pixel

coverage = collections.defaultdict(int)

for rect in rects:
    points = [(x, y) for x in range(rect.x, rect.x + rect.w) for y in range(rect.y, rect.y + rect.h)]

    for point in points:
        coverage[point] += 1

print('Coverage construction completed')

print('Answer 1: ', len(list(filter(lambda y : y > 1, coverage.values()))))

# Part 2

# Find the claim that doesn't overlap with any other.

# For each rectangle, find its maximum cover value.
# The correct rectangle will have the max cover value of 1.

for rect in rects:
    points = [(x, y) for x in range(rect.x, rect.x + rect.w) for y in range(rect.y, rect.y + rect.h)]

    cover_vals = [ coverage[point] for point in points ]

    if max(cover_vals) == 1:
        print('Answer 2: Claim #', rects.index(rect) + 1)
        break
