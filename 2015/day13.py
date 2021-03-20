import re
import itertools
f = open('day13in.txt')
lines = [line.strip() for line in f.readlines()]

reg = r'(\w*) would (\w*) (\d*) happiness units by sitting next to (\w*).'

units = {}
names = set()

for line in lines:
    m = re.match(reg, line)
    # print(line)
    # print(m.groups())

    p1, opt, amt, p2 = m.groups()
    amt = int(amt) * (1 if opt=='gain' else -1)

    units[p1+p2] = amt
    names.add(p1)
    names.add(p2)

def total_units(perm):
    total = 0

    for i in range(len(perm) - 1):
        p1 = perm[i]
        p2 = perm[i+1]
        total += units[p1+p2] 
        total += units[p2+p1] 

    # loop around
    p0 = perm[0]
    plast = perm[-1]

    total += units[p0+plast]
    total += units[plast+p0]

    return total

print('Ans 1:', max(total_units(perm) for perm in itertools.permutations(names)))

# Part 2: add yourself
for name in names:
    units['yourself'+name] = 0
    units[name+'yourself'] = 0
names.add('yourself')

print('Ans 2:', max(total_units(perm) for perm in itertools.permutations(names)))