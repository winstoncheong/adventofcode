import re
import collections

f = open('day4in_sorted.txt','r')
lines = f.readlines()


re_guard_change = r'Guard \#(\d*) begins shift'
re_fall_asleep = r'00:(\d{2})\] falls asleep'
re_wakes_up = r'00:(\d{2})\] wakes up'

# dictionary of guard => list of mins when asleep
sleep_data = collections.defaultdict(list)


guard = 0
sleep_start = 0

for line in lines:
    match = re.search(re_guard_change, line)
    
    if match: # guard change
        guard = int(match.group(1))


    match = re.search(re_fall_asleep, line)
    if match: # guard fell asleep
        sleep_start = int(match.group(1))

    match = re.search(re_wakes_up, line)
    if match: # guard wakes up
        wake_up = int(match.group(1))

        # add minutes when guard is asleep
        for i in range(sleep_start, wake_up):
            sleep_data[guard].append(i)

print('Guard data read in')


# Find guard with most minutes asleep
sleep_max = 0
guard = 0
sleep_mins = []

for k, v in sleep_data.items():
    mins_asleep = len(v)
    if mins_asleep > sleep_max:
        sleep_max = mins_asleep
        guard, sleep_mins = k,v

# Use counter to find the most common minute asleep
ctr = collections.Counter(sleep_mins)
minute = ctr.most_common(1)[0][0]

print('Answer 1:', guard * minute)

# Part 2

# Find guard that is most frequently asleep on the same minute

max_freq = 0
guard = 0
minute = 0
for k, v in sleep_data.items():
    ctr = collections.Counter(v)
    freq = ctr.most_common(1)[0][1] # get frequency of the most common minute
    if freq > max_freq:
        guard = k
        minute = ctr.most_common(1)[0][0]
        max_freq = freq

print('Answer 2:', guard * minute)
