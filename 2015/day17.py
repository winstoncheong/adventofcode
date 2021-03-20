from more_itertools import powerset

f = open('day17in.txt')
vals = list(map(int, f.readlines()))

# print(vals)

print('Answer 1:', len([ p for p in powerset(vals) if sum(p) == 150]))

# Part 2
def can_fit150(vals):
    for p in powerset(vals):
        if sum(p) == 150:
            return True
    return False

def complement(full, sub):
    comp = full.copy()
    for i in sub:
        comp.remove(i)
    return comp

min_containers = min([len(p) for p in powerset(vals) if sum(p) == 150])

count = 0
for p in powerset(vals):
    if sum(p) == 150 and len(p) == min_containers and can_fit150(complement(vals, p)):
        # print(p, complement(vals, p))
        count += 1

print('Answer 2:', count)