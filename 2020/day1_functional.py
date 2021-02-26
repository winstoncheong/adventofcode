import itertools

f = open('day1in.txt','r')
lines = f.readlines()
vals = [ int(line.strip()) for line in lines]
vals.sort()

# every 2-tuple is in this list
# [(1, 2), (3, 4), (2, 4), ....]
two_tuples = itertools.combinations(vals, 2)

res = list(filter(lambda x: x[0]+x[1]==2020, two_tuples))
print(res)

three_tuples = itertools.combinations(vals, 3)
res = list(filter(lambda x: x[0]+x[1]+x[2]==2020, three_tuples))
print(res)