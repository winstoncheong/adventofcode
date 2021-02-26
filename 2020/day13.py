import math
f = open('day13in.txt')

lines = f.readlines()

start = int(lines[0])
trains = list(map(int,filter(str.isnumeric, lines[1].split(','))))

print(start, trains)

next_train_times = [(math.floor(start/train)+1)*train for train in trains]
print(next_train_times)

next_train_time = min(next_train_times)

train_id = trains[next_train_times.index(next_train_time)]

print('Ans 1: ', train_id * (next_train_time - start))