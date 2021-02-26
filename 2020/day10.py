from collections import Counter

#f = open('testin.txt')
f = open('day10in.txt')
vals = sorted(map(int, f.readlines()))

# Add connection to wall and to device
vals.insert(0, 0)
vals.append(max(vals) + 3)

# generate successive difference list
dif = [j-i for i,j in zip(vals[:-1], vals[1:])]

print(vals)
print(dif)

ctr = Counter(dif)
print(ctr)
print("Ans 1: ", ctr[3]* ctr[1])


def count_arrangements(start, remain):
    """Start is number starting from.
    Remain is a list of possible adapters left.
    Assume that remain is sorted. 

    Only use this for brute-force computation
    """
    val = 0
#    print("Started start=",start)

    if len(remain) == 0:
        return 1

    # try 1, 2, and 3 larger than start

    if start +1 in remain:
        remain = remain[1:]
        val += count_arrangements(start+1, remain)

    if start+2 in remain:
        remain = remain[1:]
        val += count_arrangements(start+2, remain)

    if start+3 in remain:
        remain = remain[1:]
        val += count_arrangements(start+3, remain)

    #print("Finished start=",start)


    return val

# count_arrangements does not need leading 0
#print(count_arrangements(0, vals[1:])) 

def count_consecutive_ones(dif):
    ans = []
    count = 0
    for i in range(len(dif)):
        if dif[i]==1:
            count += 1

        else:
            ans.append(count)
            count = 0
    return ans

def compute_arrangements(lst):
    """Give list of consecutive ones, can compute arrangements using rules
    """

    arr = 1 

    for i in lst:
        if i == 2:
            arr *= 2
        elif i == 3:
            arr *= 4
        elif i == 4:
            arr *= 7
        elif i > 4:
            print("Error. Need to account for ", i)
        

    return arr



print(count_consecutive_ones(dif))
print('Ans 2: ', compute_arrangements(count_consecutive_ones(dif)))


