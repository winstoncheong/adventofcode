f = open('day1in.txt','r')

lines = list(map(int,f.readlines()))

# sum up all changes in frequency 
print("Ans 1: ", sum(lines))

freq = set([0])
curr = 0
while True:

    for val in lines:
        curr += val
        # print(curr)
        if curr in freq:
            print("Ans 2: ", curr)
            break
            
        else: 
            freq.add(curr)

    # design pattern used to break outer loop from inner
    else:
        continue
    break
    
