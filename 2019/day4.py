from collections import Counter 

def is_valid1(value):
    string = str(value)
    
    adjacent = False
    decrease = False
    
    for i in range(len(string) - 1):
        if string[i] == string[i+1]: # need two adjacent
            adjacent = True
        elif string[i+1] < string[i]: # should never decrease
            decrease = True 

    return adjacent and not decrease

def is_valid2(value):
    string = str(value)
    
    adjacent = False
    decrease = False
    
    for i in range(len(string) - 1):
        if string[i] == string[i+1]: # need two adjacent
            adjacent = True
        elif string[i+1] < string[i]: # should never decrease
            decrease = True 

    # there must be a pair
    count = Counter(string)
    values = count.values()

    if 2 not in values:
        return False

    return adjacent and not decrease
    

# print(is_valid(111111))
# print(is_valid(223450))
# print(is_valid(123789))
# print(is_valid(123444))
# print(is_valid(111122))

count = 0
for i in range(372304,847060+1):
    if is_valid1(i):
        count += 1

print(f'Answer 1: {count}')

count = 0
for i in range(372304,847060+1):
    if is_valid2(i):
        count += 1

print(f'Answer 2: {count}')