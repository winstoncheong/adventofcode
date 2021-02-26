import re 
from collections import Counter

# 7-10 w: mlwcwgwwbcbwggwwgwwn
PATTERN = '^(\d+)-(\d+) (\w): (\w+)$'
f = open('day2in.txt','r')
#f = open('testin.txt','r')
lines = f.readlines()

a1 = 0
a2 = 0

for line in lines:
	line = line.strip()
	# print(line)
	m = re.search(PATTERN, line)
	# print(m.groups())
	g = m.groups()

	pw = g[3]
	char = g[2]


	# check validity of string for part 1
	c = Counter(pw) # count letters in the string.
	if int(g[0]) <= c[char] <= int(g[1]):
		a1 += 1

	# part 2
	i1 = int(g[0])-1
	i2 = int(g[1])-1
	if (pw[i1] == char) ^ (pw[i2] == char):
		a2+=1
	

print("Ans 1:", a1)
print("Ans 2:", a2)


