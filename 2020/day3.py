import itertools
from functools import reduce
import operator

f = open('day3in.txt','r')
trees = f.readlines()
trees = [line.strip() for line in trees] # sanitize 

# data about the map of trees
m = len(trees[0])  # modulus
h = len(trees) # height


def count_trees(r, d):
    """
    r = amount travelled right
    d = amount travelled down
    """

    xpos = 0
    ypos = 0
    count = 0 # count number of trees encountered


    while ypos < h:
        row = trees[ypos]
        ch = row[xpos % m]

        if ch == '#': # is tree
            count += 1
        
        # follow slope
        xpos += r
        ypos += d

    return count



print('Ans 1: ', count_trees(3, 1))

# slopes to test
slopes = [(1,1), (3, 1), (5, 1), (7, 1), (1, 2)]

# use starmap to depack the tuples that get passed to count_trees
counts = list(itertools.starmap(count_trees, slopes))

# Because Python does not have a prod() function analogous to sum(), this incantation is needed
ans2 = reduce(operator.mul, counts, 1)

#print(counts)
print("Ans 2: ", ans2)
