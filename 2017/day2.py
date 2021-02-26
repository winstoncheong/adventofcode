
with open('day2input.txt') as f:
    lines = f.readlines()

answer1 = 0
for line in lines:
    # print(line)
    vals = list(map(int, line.strip().split()))

    minval = min(vals)
    maxval = max(vals)

    answer1 += maxval - minval

print(f'Answer 1: {answer1}')

answer2 = 0
for line in lines:
    # print(line)
    vals = list(map(int, line.strip().split()))
    vals.sort()
    
    # find two numbers that are divisible
    for i in range(len(vals)):
        for j in range(i+1, len(vals)):
            if vals[j] % vals[i] == 0:
                # print(vals[j], vals[i], vals[j]//vals[i])
                answer2 += vals[j] // vals[i]
               

print(f'Answer 2: {answer2}')
