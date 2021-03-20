import re
from collections import defaultdict
from collections import Counter
from more_itertools import flatten

reg = r'(\w*) can fly (\d*) km/s for (\d*) seconds, but then must rest for (\d*) seconds.'

f = open('day14in.txt')
lines = f.readlines()

simulation_length = 2503

def simulate(length, fly, fly_duration, rest_duration):
    dist = 0
    while length > 0:
        # fly phase
        amt = min(length, fly_duration)
        dist += fly * amt
        length -= amt

        # rest phase
        amt = min(length, rest_duration)
        length -= amt
    return dist

deer_data = []
distances = []

for line in lines:
    m = re.match(reg, line)
    name, fly, fly_duration, rest_duration = m.groups()
    deer_data.append((name, int(fly), int(fly_duration), int(rest_duration)))

for name, fly, fly_duration, rest_duration in deer_data:
    distances.append(simulate(simulation_length, fly, fly_duration, rest_duration))

print('Ans 1:', max(distances))

# Part 2
class Reindeer:
    def __init__(self, name, fly, fly_duration, rest_duration):
        self.name = name
        self.fly = fly
        self.fly_duration = fly_duration
        self.rest_duration = rest_duration 

        self.state = 'flying'
        self.remaining_time = fly_duration
        self.dist = 0

    def step(self):
        self.remaining_time -= 1

        if self.state == 'flying':
            self.dist += self.fly
            if self.remaining_time == 0:
                self.state = 'resting'
                self.remaining_time = self.rest_duration
    
        if self.state == 'resting':
            if self.remaining_time == 0:
                self.state = 'flying'
                self.remaining_time = self.fly_duration

    def __repr__(self):
        return f'Reindeer({self.name}, fly={self.fly}, fly_duration={self.fly_duration}, rest_duration={self.rest_duration}, dist={self.dist}, state={self.state}, remaining_time={self.remaining_time})'

deers = []

def simultaneous_step():
    """Take a step, return winner(s)"""

    dist = defaultdict(list)
    for d in deers:
        d.step()
        dist[d.dist].append(d.name)

    winner = dist[max(dist.keys())]
    # print(f'Winners: {winner} with distance {max(dist.keys())}')
    return winner
    
# Initialize reindeer objects
for data in deer_data:
    deers.append(Reindeer(*data))

winner_aggregate = []

for i in range(simulation_length):
    winner_aggregate.append(simultaneous_step())

ctr = Counter(flatten(winner_aggregate))
print('Answer 2:', ctr.most_common(1))