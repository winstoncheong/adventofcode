import json
f = open('day12in.txt')
line = f.readline()

out = json.loads(line)

def sum_all(structure, part):
    if type(structure) is dict:
        if 'red' in structure.values() and part==2: 
            return 0

        return sum(sum_all(sub, part) for sub in structure.values())
    elif type(structure) is list:
        return sum(sum_all(sub, part) for sub in structure)
    elif type(structure) is int:
        return structure
    elif type(structure) is str:
        return 0
    else:
        print(type(structure))
        return 0

print('Ans 1: ', sum_all(out, 1))
print('Ans 2: ', sum_all(out, 2))