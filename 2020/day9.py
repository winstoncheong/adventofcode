
sliceLen = 26

f = open('day9in.txt')
vals = list(map(int, f.readlines())) 

#print(vals)


def check(lst):
    """Check whether the last number can be produced from adding two previous numbers"""
    for i in lst:
        for j in lst:
            if i+j == lst[-1]:
                return True
    return False


# Part 1
val = 0
for i in range(0, len(vals)-sliceLen + 1):
    sublist = vals[i:i+sliceLen]

    if check(sublist):
        continue
    else:
        val = sublist[-1] 
        print('Ans 1:', val)

# Part 2
for i in range(0, len(vals)): 
    for j in range(i+2, len(vals)):  # don't produce sublist of length 1
        sublist = vals[i:j]
        if sum(sublist) > val: # break j-loop
            break
        if sum(sublist) == val:
            print('Ans 2', min(sublist) + max(sublist))
            # print(sublist)
            break
