import re 
from pprint import pprint
from collections import defaultdict

#f =  open('testin.txt')
f =  open('day7in.txt')
rules = [line.strip() for line in f.readlines()]

# child => containers
containment = defaultdict(set)

# parent => [(num, ident)]
children = defaultdict(list)

#print(rules[1:10])

for rule in rules:
    parent, childs = rule.split('contain')
    #print(parent, childs)

    #print('test child:')
    for child in childs[:-1].split(','):
        child = child.strip()
        #print(child)
        parts = child.split(' ')
        #print(parts)
        if len(parts) == 4:
            
            childName = ' '.join(parts[1:3])
            parentName = ' '.join(parent.split(' ')[0:2])

            #print(f'{childName} => {parentName}')

            containment[childName].add(parentName)

            # part 2:
            amt = int(parts[0])
            children[parentName].append((amt, childName))


#print(containment)
#pprint(children)

ancestors = set()
to_process = list(containment["shiny gold"])

while len(to_process) != 0:
    ancestor = to_process.pop()
    ancestors.add(ancestor)
    to_process.extend(containment[ancestor])

print('Ans 1:', len(ancestors))

# Part 2

def count_children(node):
    ch = children[node]
    count = sum(tup[0] for tup in ch)  # start count with number of direct descendents

    for tup in ch:
        count += tup[0] * count_children(tup[1])

    #print(count)
    return count


print('Ans 2:',  count_children('shiny gold'))
