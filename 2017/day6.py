
with open('day6input.txt') as f:
    line = f.readline().strip()
    line = [ int(val) for val in line.split() ]


# line=[0, 2, 7, 0] # Test input

# print(line)

def redistribute(line):
    amt = max(line)
    index = line.index(amt)
    line[index]=0
    
    while amt > 0:
        index+= 1
        if index >= len(line): # wraparound
            index = 0

        line[index] += 1
        amt -= 1
    
#    print(line)

seen = []
cycles = 0
config = ','.join(str(_) for _ in line)


while config not in seen:
    seen.append(config)
    redistribute(line)
    cycles += 1
    config = ','.join(str(_) for _ in line)

print(f'Answer 1: {cycles}')
print(f'Answer 2: {cycles - seen.index(config)}')
