input = '0,5,4,1,10,14,7'
testin = '0,3,6'


vals = list(map(int, input.split(',')))

# num -> last occurrence
last_index = {}
next_val = 0

dist = -1

# process all input first
# assume vals doesn't have repeat numbers
for i, val in enumerate(vals):
    last_index[val] = i + 1

count = len(vals)

# look up the last_index of the last_val, subtract from count to arrive at new_value
# update last_index with new_value:
#   if not previously there, gets added to last_index and new_value becoems 0. 
#   if is there, compute count - last_index[new_val] which is the new_val. 

while True:
    # about to insert next_val. Compute distance to find new next_val

    if next_val not in last_index.keys():
        new_next_val = 0
        #print('New value: ', next_val)
    else:
        new_next_val = count + 1 - last_index[next_val]
    
    # "speak" the next value
    count +=1
    #print(f'Index: {count}, Speak: {next_val}') 

    if count == 2020:
        print('Ans 1: ', next_val)
    if count % 1000000 == 0:
        print(f"Reached {count/1000000} million")
    if count == 30000000:
        print('Ans 2: ', next_val) 
        break

    last_index[next_val] = count
    next_val = new_next_val 


print(next_val)



# First attempt

# def rindex(mylist, myvalue):
#     try:
#         ret = len(mylist) - mylist[::-1].index(myvalue) - 1
#     except:
#         return -1
#     return ret

# while(len(vals) <= 2020):
#     last = vals[-1]
#     index = rindex(vals[:-1], last)

#     if(index == -1):
#         vals.append(0)
#     else:
#         vals.append(len(vals) - index - 1)

# print(vals[2020-1])


