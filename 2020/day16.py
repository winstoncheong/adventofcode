from pprint import pprint

#f = open('testin.txt')
f = open('day16in.txt')
lines = [line.strip() for line in f.readlines()]

# str -> list(range)
rules = {}

all_ranges = [] # simpler version for part 1
your_ticket = []
nearby_tickets = []

part = 0

def make_range(input):
    """Given a string num1-num2, return a range object range(num1, num2+1)"""

    vals = list(map(int, input.split('-')))
    return range(vals[0], vals[1]+1)

# read in data
for line in lines:
    if line == '':
        continue

    if line == 'your ticket:':
        part = 1
        continue

    if line == 'nearby tickets:':
        part = 2
        continue

    if part == 0:
        parts = line.split(':')
        ranges = parts[1].split("or")
        #print(ranges)
        for valid in ranges:
            all_ranges.append(make_range(valid))

        # part 2 additions
        ident = parts[0]
        vals = list(map(make_range, ranges))
        #print(vals)
        rules[ident] = vals

    
    elif part == 1:
        your_ticket = list(map(int, line.split(',')))

    elif part == 2:
        ticket = list(map(int, line.split(',')))
        nearby_tickets.append(ticket)

def ticket_error(lst):
    """list(int) -> int.
    Returns the sum of invalid ticket fields. Returns 0 if all valid
    """
    ret = 0
    for field in lst:
        for range in all_ranges:
            if field in range:
                break
        else: # field is invalid
            ret += field

    return ret

def ticket_valid(lst):
    """list(int) -> bool. False if any ticket field is not in acceptable range"""

    for field in lst:
        for range in all_ranges:
            if field in range:
                break
        else: # field invalid
            return False
    return True

# print(all_ranges)

print('Ans 1: ', sum(map(ticket_error, nearby_tickets)))

# part 2
valid_tickets = []
for ticket in nearby_tickets:
    if ticket_valid(ticket):
        valid_tickets.append(ticket)

# print(rules)
# print(valid_tickets)

def possible_fields(nums):
    '''Given column of numbers, returns field names whose rules fit these numbers.
    '''
    possible = []
    for k,v in rules.items():
        for num in nums:
            if num not in v[0] and num not in v[1]:
                # value is invalid for this field-type
                break 
        else: # all nums work for this field-type
            possible.append(k)

    return possible


# determine association from field_number to field_name
associations = {}

columns = zip(*valid_tickets)
for i, column in enumerate(columns):
    associations[i] = possible_fields(column)

# print(associations)

def is_fully_simplified(associations):
    for k, v in associations.items():
        if len(v) > 1:
            return False
    return True


def simplify_associations1(associations):
    # First simplification: Any column with only one option, must be that option. 
    # Remove option from all other.

    # list of tuples (column, field_type)
    determined = {}
    stalled = False

    while not stalled:
        stalled = True
        for k,v in associations.items():
            if len(v) == 1 and k not in determined:
                stalled = False
                determined[k] = v[0]
                #print("Found", k, v)
        #print(determined)
        for column, field_type in determined.items():
            for k,v in associations.items():
                if k != column and field_type in v:
                    #print(f'Found extra "{field_type}" in {k}=>{v}')
                    v.remove(field_type) # does this modify entry in dictionary?

    return associations

def simplify_associations2(associations):
    # Second simplification: If a field_type shows up only in one column, the column must be that field_type
    # Remove all other options from that column.

    determined = {}
    # Populate determined
    for k,v in associations.items():
        if len(v) == 1:
            determined[k] = v[0]

    stalled = False

    while not stalled: 
        stalled = True
        for field_type in rules.keys():
            #print(field_type)
            columns_containing = [column for column, field_types in associations.items() if field_type in field_types]
            #print(columns_containing)
            column = columns_containing[0]
            if column not in determined and len(columns_containing) == 1:
                associations[column] = [field_type] # set 
                determined[column] = field_type
                stalled = False

    return associations

# print("After simplification 1")
associations = simplify_associations1(associations)
# pprint(associations)

# print('After simplification 2')
associations = simplify_associations2(associations)
# pprint(associations)


if is_fully_simplified(associations):
    print("Associations are fully simplified!")
else:
    print("Associations are NOT fully simplified!")

ans2 = 1    
for column, field in associations.items():
    if field[0].startswith('departure'):
        ans2 *= your_ticket[column]

print('Ans 2: ', ans2)
