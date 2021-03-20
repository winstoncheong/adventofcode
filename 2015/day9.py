from itertools import permutations

f = open('day9in.txt')

lines = f.readlines()

cities = set()
distances = dict()

for line in lines:
    parts = line.split()
    city1 = parts[0]
    city2 = parts[2]
    dist = int(parts[4])

    cities.add(city1)
    cities.add(city2)
    # print(city1, city2, dist)

    distances[city1+city2] = dist
    distances[city2+city1] = dist

def trip_dist(trip):
    dist = 0
    for i in range(len(trip) - 1):
        city1 = trip[i]
        city2 = trip[i+1]
        dist += distances[city1+city2]
    return dist

print('Ans 1:', min(trip_dist(perm) for perm in permutations(cities)))
print('Ans 2:', max(trip_dist(perm) for perm in permutations(cities)))