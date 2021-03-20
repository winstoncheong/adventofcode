import enum
import re

f = open('day16in.txt')
lines = f.readlines()

sue_wanted = {'children': 3, 
    'cats': 7, 
    'samoyeds': 2, 
    'pomeranians': 3, 
    'akitas': 0, 
    'vizslas': 0, 
    'goldfish': 5, 
    'trees': 3, 
    'cars': 2, 
    'perfumes': 1}

sues = []

for line in lines:
    m = re.match(r'Sue \d*: (.*)', line)

    data = m.group(1).split(', ')

    sue = {}

    for keyval in data:
        key, val = keyval.split(': ')
        sue[key] = int(val)
    
    sues.append(sue)

def sue_matches_1(sue):
    for k, v in sue.items():
        if v != sue_wanted[k]:
            return False
    return True

def sue_matches_2(sue):
    for k, v in sue.items():
        if k == 'cats' or k == 'trees':
            if v <= sue_wanted[k]: # should be greater than the sue_wanted amount
                return False
        elif k == 'pomeranians' or k == 'goldfish':
            if v >= sue_wanted[k]: # should be less than the sue_wanted amount
                return False
        else:
            if v != sue_wanted[k]:
                return False
    return True


for i, sue in enumerate(sues):
    if sue_matches(sue):
        print('Ans 1:', i+1)
    if sue_matches_2(sue):
        print('Ans 2:', i+1)