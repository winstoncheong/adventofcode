
with open('day4input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

def is_valid1(line):
    """A line is not valid if it contains duplicate words"""
    words = line.split()
    return len(words) == len(set(words))

def is_valid2(line):
    """A line is not valid if any word can be rearranged into another word"""

    # sort all the words and apply uniqueness check

    sorted_words = [ "".join(sorted(word)) for word in line.split()]
    return len(sorted_words) == len(set(sorted_words))
    

count1 = 0
count2 = 0
for line in lines:
    if is_valid1(line):
        count1 += 1
    if is_valid2(line):
        count2 += 1


print(f'Answer 1: {count1}')
print(f'Answer 2: {count2}')
