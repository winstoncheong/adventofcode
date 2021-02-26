
f = open("day5in.txt")
lines = f.readlines()

def pass_to_ID(boarding):
    row = int(boarding[0:7].replace("F","0").replace("B","1"), 2)
    col = int(boarding[7:].replace("R","1").replace("L","0"), 2)
    return 8 * row + col

# Part 1
maxval = max(map(pass_to_ID, lines))
print("Ans 1: ", maxval)

# Part 2

ids = sorted(list(map(pass_to_ID, lines)))
# print(ids)

# Find what ids are missing from the list we're given
diff = set(range(maxval)).difference(set(ids))
print(diff)
 
# By inspection, can see which number sticks out (does not have its neighbors)
