from collections import namedtuple

f = open('day12in.txt')
lines = [line.strip() for line in f.readlines()]

# direction, in degrees counterclockwise 
dir = 0 
x=0
y=0

# Part 1
for line in lines:
    cmd = line[0]
    amt = int(line[1:])

    if cmd=='N':
        y += amt
    elif cmd=='S':
        y -= amt
    elif cmd=='E':
        x += amt
    elif cmd=='W':
        x -= amt
    elif cmd=='L':
        dir += amt
        dir %= 360
    elif cmd=='R':
        dir -= amt
        dir %= 360
    elif cmd=='F':
        if dir==0:
            x += amt
        elif dir==90:
            y += amt
        elif dir==180:
            x -= amt
        elif dir==270:
            y -= amt
        else:
            print("Direction: ", dir)
    else:
        print("Cmd: ", cmd)

print("Ans 1: ", abs(x)+abs(y))


# Part 2

# reset values
dir = 0 # not used for part 2
x=0
y=0
Point = namedtuple('Point', ['x', 'y'])
waypoint = Point(10, 1)

def rotate_waypoint(cmd, amt):
    global waypoint

    if (cmd=='R' and amt==90) or (cmd=='L' and amt==270):
        waypoint = Point(waypoint.y, -waypoint.x)
    elif (cmd=='L' and amt==90) or (cmd=='R' and amt==270):
        waypoint = Point(-waypoint.y, waypoint.x)
    elif (cmd=='L' and amt==180) or (cmd=='R' and amt==180):
        waypoint = Point(-waypoint.x, -waypoint.y)
    else:
        print("Error: ", cmd, amt)


for line in lines:
    cmd = line[0]
    amt = int(line[1:])

    if cmd=='N':
        waypoint = Point(waypoint.x, waypoint.y+amt)
    elif cmd=='S':
        waypoint = Point(waypoint.x, waypoint.y-amt)
    elif cmd=='E':
        waypoint = Point(waypoint.x+amt, waypoint.y)
    elif cmd=='W':
        waypoint = Point(waypoint.x-amt, waypoint.y)
    elif cmd=='L' or cmd == 'R':
        rotate_waypoint(cmd, amt)
    elif cmd=='F':
        x += waypoint.x * amt
        y += waypoint.y * amt
    else:
        print("Cmd: ", cmd)


print("Ans 2: ", abs(x)+abs(y))