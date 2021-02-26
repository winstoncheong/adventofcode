from collections import Counter
import re

f = open('day5in.txt')

lines = f.readlines()

def is_nice(string):
    ctr = Counter(string)

    vowels = ctr['a'] + ctr['e'] + ctr['i'] + ctr['o'] + ctr['u']
    if vowels < 3: 
        return False
    
    # need twice in a row
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            break
    else:
        return False # no twice in a row

    disallowed = ['ab', 'cd', 'pq', 'xy'] 
    for substr in disallowed:
        if substr in string:
            return False
    
    return True

# print(is_nice('ugknbfddgicrmopn'))
# print(is_nice('jchzalrnumimnmhp'))
# print(is_nice('haegwjzuvuyypxyu'))
# print(is_nice('dvszwmarrgswjxmb'))

ans1 = 0
for line in lines:
    if is_nice(line):
        ans1 += 1

print('Ans 1:', ans1)


# Part 2

regex1 = r'(\w{2}).+\1'
regex2 = r'(\w)\w\1'

def is_nice2(string):
    match1 = re.search(regex1, string)
    match2 = re.search(regex2, string)
    if match1 and not match2:
        print(string, 'matches only condition 1 with match ', match1.group(0))
    if match2 and not match1:
        print(string, 'matches only condition 2 with match', match2.group(0))
    if match1 and match2: 
        print(string, 'matches both')

    return match1 and match2

print(is_nice2('aaa'))
print(is_nice2('qjhvhtzxzqqjkmpb'))
print(is_nice2('xxyxx'))
print(is_nice2('uurcxstgmygtbstg'))
print(is_nice2('ieodomkazucvgmuy'))

ans2 = 0
for line in lines:
    if is_nice2(line):
        ans2 += 1

print('Ans 2:', ans2)