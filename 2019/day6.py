import collections

parent = collections.defaultdict(list)

f = open('day6in.txt','r')
# f = open('test.in','r')

lines = f.readlines()

# init parent map
for line in lines:
    parts = line.strip().split(")")
    parent[parts[1]].append(parts[0])
#print(parent)

# count orbits
# orbits = 0
# keys = list(parent.keys())

# for i in range(len(keys)):
#     key = keys[i]
#     while(parent[key]):
#         key = parent[key][0]
#         orbits += 1
    
# print(orbits)

def make_parents(ident):
    parents = list()
    while(parent[ident]):
        ident = parent[ident][0]
        parents.append(ident)
    return parents

p1 = make_parents('SAN')
p2 = make_parents('YOU')

print(p1)
print(p2)

for item in p1:
    if item in p2:
        print(item)
        print(p1.index(item))
        print(p2.index(item))
        break

# final answer: add the two indexes. 