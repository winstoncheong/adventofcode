
f = open('day6in.txt')
lines = [line.strip() for line in f.readlines()]
lines.append("") # make last group

count1 = 0
count2 = 0

some_ans = set()
all_ans = set()

# groups is a list of lists, where each element is the individual group
groups = []

group = []

# regroup.

for line in lines:
    if line == '':
        # found end of group
        groups.append(group)
        group = []

    else:
        group.append(line)


for group in groups:
    # part 1: count set union
    union = set("".join(group))
    count1 += len(union)

    # part 2: count set intersection

    intersection = union # start with all characters
    for member in group:
        intersection = intersection.intersection(set(member))

    count2 += len(intersection)

print("Ans 1: ", count1)
print("Ans 2: ", count2)
