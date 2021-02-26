import collections

f = open('day2in.txt','r')

lines = f.readlines()
lines = [line.strip() for line in lines]


count_double = 0
count_triple = 0

def hamming_distance(string1, string2):
    dist_counter = 0
    for n in range(len(string1)):
        if string1[n] != string2[n]:
            dist_counter += 1
    return dist_counter

# Part 1
for line in lines:
    ctr = collections.Counter(line)
    if(2 in ctr.values()):
        count_double += 1
    if(3 in ctr.values()):
        count_triple += 1

print("Ans 1: ", count_double * count_triple)

# Part 2
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        if(hamming_distance(lines[i], lines[j]) == 1):
            # found the two box IDs
            
            ans2 = ""
            for c in range(len(lines[i])):
                if lines[i][c] == lines[j][c]:
                    ans2 += lines[i][c]

            print("Ans 2: ", ans2)
            break
